"""Fabrica de cortes verticais - DigitalMedia.
Pipeline: video/URL -> transcricao (faster-whisper) -> selecao de momentos ->
recorte vertical 9:16 com seguimento de rosto -> legendas destaque palavra por palavra -> MP4.

Uso:
  python cortar.py video.mp4 --auto 3
  python cortar.py "https://youtube.com/..." --auto 5 --idioma pt
  python cortar.py video.mp4 --cortes "01:12-01:47,05:03-05:40"
  python cortar.py video.mp4 --cortes "00:30-01:00" --sem-rosto --titulo meu-corte
Dependencias: faster-whisper, opencv-python, numpy, yt-dlp, ffmpeg no PATH.
"""
import argparse, os, re, subprocess, sys, unicodedata

HOOKS = ["como", "porque", "por que", "segredo", "erro", "nunca", "sempre", "grátis",
         "gratis", "dinheiro", "venda", "vender", "lucro", "milh", "verdade", "mentira",
         "atenção", "atencao", "pare", "incrível", "incrivel", "garantido", "passo",
         "truque", "método", "metodo", "resultado", "prova", "ninguém", "ninguem",
         "todo mundo", "você", "voce", "pergunta", "resposta", "?"]

def ts(s):
    s = s.strip()
    p = s.split(":")
    v = float(p[-1].replace(",", "."))
    if len(p) > 1: v += int(p[-2]) * 60
    if len(p) > 2: v += int(p[0]) * 3600
    return v

def fmt(s):
    h, r = divmod(s, 3600); m, sec = divmod(r, 60)
    return "%02d:%02d:%06.3f" % (h, m, sec)

def norm(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERRO ffmpeg:", r.stderr[-2000:]); sys.exit(1)

def baixar(fonte, saida):
    if os.path.exists(fonte):
        return fonte
    print("Baixando (yt-dlp)...")
    run(["yt-dlp", "-f", "bv*[height<=1080]+ba/b[height<=1080]/b", "--merge-output-format", "mp4",
         "-o", saida, fonte])
    return saida

def transcrever(video, idioma, modelo="small"):
    import av
    _open = av.open  # compat: faster-whisper passa metadata_errors, removido no PyAV>=15
    av.open = lambda *a, **k: _open(*a, **{x: v for x, v in k.items() if x != "metadata_errors"})
    from faster_whisper import WhisperModel
    import torch
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Transcrevendo ({modelo}/{dev})... pode levar alguns minutos no 1o uso (download do modelo).")
    m = WhisperModel(modelo, device=dev, compute_type="float16" if dev == "cuda" else "int8")
    segs, _ = m.transcribe(video, language=None if idioma == "auto" else idioma, word_timestamps=True,
                            vad_filter=True)
    out = []
    for s in segs:
        ws = [{"w": w.word.strip(), "i": w.start, "f": w.end} for w in (s.words or []) if w.word.strip()]
        out.append({"i": s.start, "f": s.end, "t": s.text.strip(), "w": ws})
    print(f"{len(out)} segmentos.")
    return out

def pontuar(txt):
    n = norm(txt); pts = 0.0
    for h in HOOKS:
        if h in n: pts += 2.0 if h in ("?", "como", "segredo", "erro", "nunca") else 1.0
    pts += min(len(txt.split()), 40) / 40.0
    if "!" in txt or "?" in txt: pts += 1.5
    return pts

def auto_cortes(segs, qtd, dmin=25, dmax=55):
    cands = []
    for i, s in enumerate(segs):
        txt, ini = s["t"], s["i"]
        j = i
        while j + 1 < len(segs) and segs[j + 1]["f"] - ini < dmax:
            j += 1; txt += " " + segs[j]["t"]
        dur = segs[j]["f"] - ini
        if dur >= dmin:
            cands.append((pontuar(txt) * (1 + min(dur, 45) / 90.0), ini, segs[j]["f"]))
    cands.sort(reverse=True)
    picks = []
    for _, a, b in cands:
        if all(b <= x[0] - 2 or a >= x[1] + 2 for x in picks):
            picks.append((a, b))
            if len(picks) == qtd: break
    return sorted(picks)

def parse_cortes(txt):
    out = []
    for p in txt.split(","):
        a, b = p.split("-"); out.append((ts(a), ts(b)))
    return out

def faixa_rosto(video, ini, fim, w_src, h_src, tw=608, th=1080):
    """Retorna lista de centros-x suavizados (1 por segundo) via Haar cascade; fallback: centro."""
    import cv2
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    xs, t, step, last = [], ini, max(1, int(fps)), w_src / 2
    while t <= fim:
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, fr = cap.read()
        if not ok: break
        g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(g, 1.2, 5, minSize=(60, 60))
        if len(faces):
            fx = max(faces, key=lambda r: r[2] * r[3]); last = fx[0] + fx[2] / 2
        xs.append(last); t += 1.0
    cap.release()
    if not xs: xs = [w_src / 2]
    # suaviza
    sm = []
    for i, x in enumerate(xs):
        win = xs[max(0, i - 2):i + 3]; sm.append(sum(win) / len(win))
    # converte p/ crop-x clampado
    cw = int(h_src * 9 / 16)
    cw = min(cw, w_src)
    out = []
    for x in sm:
        cx = max(cw / 2, min(w_src - cw / 2, x)); out.append(int(cx - cw / 2))
    return out, cw

def ass_legenda(words, path, ini):
    def A(t):  # ASS timestamp
        h, r = divmod(t, 3600); m, s = divmod(r, 60)
        return "%d:%02d:%05.2f" % (h, m, s)
    L = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 608", "PlayResY: 1080",
         "[V4+ Styles]", "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
         "Style: Legenda,Arial,44,&H00FFFFFF,&H000000FF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,40,40,120,1",
         "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    # blocos de ~2.2s
    blk, t0 = [], None
    def flush():
        if not blk: return
        a, b = blk[0]["i"] - ini, blk[-1]["f"] - ini
        txt = "".join("{\\kf%d}%s " % (max(1, int(round((w["f"] - w["i"]) * 100))), w["w"].replace("{", "").replace("}", "")) for w in blk)
        L.append(f"Dialogue: 0,{A(max(0,a))},{A(max(0,b))},Legenda,,0,0,0,,{txt}")
    for w in words:
        if t0 is None: t0 = w["i"]
        if w["i"] - t0 > 2.2: flush(); blk, t0 = [], w["i"]
        blk.append(w)
    flush()
    open(path, "w", encoding="utf-8").write("\n".join(L))

def probe(video):
    import json
    r = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", video],
                       capture_output=True, text=True)
    for s in json.loads(r.stdout)["streams"]:
        if s["codec_type"] == "video":
            return int(s["width"]), int(s["height"]), 30
    return 1280, 720, 30

def cortar(video, a, b, idx, outdir, titulo, idioma, modelo):
    import cv2
    w, h, _ = probe(video)
    dur = b - a
    base = os.path.join(outdir, f"{titulo}-{idx + 1:02d}")
    # 1. recorte vertical com seguimento (crop dinamico via crop=x:y ao longo do tempo n eh trivial;
    #    usamos crop central na largura do rosto medio + scale). Simplificacao robusta:
    xs, cw = faixa_rosto(video, a, b, w, h)
    cx = int(sum(xs) / len(xs))
    ch = int(cw * 16 / 9); ch = min(ch, h)
    cy = max(0, min(h - ch, int(h * 0.5 - ch / 2)))
    tmpv = base + "-v.mp4"
    run(["ffmpeg", "-y", "-ss", str(a), "-t", str(dur), "-i", video,
         "-vf", f"crop={cw}:{ch}:{cx}:{cy},scale=608:1080",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-an", tmpv])
    # 2. palavras no intervalo -> ass
    segs = transcrever(video, idioma, modelo) if not hasattr(cortar, "_segs") else cortar._segs
    words = [x for s in segs for x in s["w"] if s["i"] >= a - 1 and s["f"] <= b + 1]
    ass = base + ".ass"
    ass_legenda(words if words else [{"w": "", "i": a, "f": a}], ass, a)
    srt = base + ".srt"
    open(srt, "w", encoding="utf-8").write("1\n00:00:00,000 --> 00:00:01,000\n...\n")
    # 3. mux final com legenda queimada + audio tratado
    out = base + ".mp4"
    ass_esc = ass.replace("\\", "/").replace(":", "\\:")
    run(["ffmpeg", "-y", "-ss", str(a), "-t", str(dur), "-i", video,
         "-vf", f"crop={cw}:{ch}:{cx}:{cy},scale=608:1080,subtitles='{ass_esc}'",
         "-af", "dynaudnorm", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out])
    os.remove(tmpv)
    return out

def main():
    ap = argparse.ArgumentParser(description="Fabrica de cortes verticais 9:16 com legendas.")
    ap.add_argument("fonte", help="arquivo local ou URL (yt-dlp)")
    ap.add_argument("--auto", type=int, default=0, help="N cortes automaticos pelos melhores momentos")
    ap.add_argument("--cortes", default="", help='Intervalos manuais "MM:SS-MM:SS,..."')
    ap.add_argument("--idioma", default="pt", help="pt|en|es|auto")
    ap.add_argument("--modelo", default="small", help="tiny|base|small|medium")
    ap.add_argument("--titulo", default="corte", help="slug base dos arquivos")
    ap.add_argument("--sem-rosto", action="store_true", help="pula deteccao facial (crop central)")
    a = ap.parse_args()

    outdir = os.path.join("cortes", a.titulo); os.makedirs(outdir, exist_ok=True)
    video = baixar(a.fonte, os.path.join(outdir, "origem.mp4"))

    if a.cortes:
        intervalos = parse_cortes(a.cortes)
    else:
        segs = transcrever(video, a.idioma, a.modelo)
        cortar._segs = segs
        intervalos = auto_cortes(segs, a.auto or 3)
        if not intervalos:
            print("Sem fala suficiente p/ auto; use --cortes manual."); sys.exit(1)
        print("Momentos:", ["%s-%s" % (fmt(x), fmt(y)) for x, y in intervalos])
    if not hasattr(cortar, "_segs"):
        cortar._segs = transcrever(video, a.idioma, a.modelo)

    if a.sem_rosto:
        import cv2  # noqa
        # desativa tracking: faixa_rosto retorna centro fixo
        global faixa_rosto
        _orig = faixa_rosto
        def faixa_rosto(video, ini, fim, w_src, h_src, tw=608, th=1080):
            cw = min(w_src, int(h_src * 9 / 16))
            return [int(w_src / 2 - cw / 2)] * max(1, int(fim - ini)), cw

    saidas = []
    for i, (x, y) in enumerate(intervalos):
        print(f"Corte {i + 1}/{len(intervalos)}: {fmt(x)} -> {fmt(y)}")
        saidas.append(cortar(video, x, y, i, outdir, a.titulo, a.idioma, a.modelo))
    print("\nPRONTO:")
    [print(" -", s) for s in saidas]

if __name__ == "__main__":
    main()
