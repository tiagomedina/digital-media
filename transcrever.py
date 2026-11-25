"""Transcricao + Redacao direto via OpenCode Go - sem n8n.
Uso: python transcrever.py "titulo" "texto bruto..."
Lê LLM_API_KEY de n8n/.env
"""
import os, sys, json, urllib.request

BASE = "https://opencode.ai/inference/go/openai/v1"
MODEL_LIMPA = "mimo-v2.6-flash"
MODEL_REDACAO = "claude-haiku-5-5"

def load_key():
    for p in [os.path.join("n8n", ".env"), os.path.join("G:/Projetos/DigitalMedia/n8n", ".env")]:
        if os.path.exists(p):
            for line in open(p, encoding="utf-8", errors="ignore"):
                if line.startswith("LLM_API_KEY="):
                    k = line.strip().split("=", 1)[1]
                    if k and "cole-sua" not in k:
                        return k
    return os.environ.get("LLM_API_KEY", "")

def chat(key, model, system, user, temp=0.5):
    body = json.dumps({"model": model, "temperature": temp,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}).encode()
    req = urllib.request.Request(BASE + "/chat/completions", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json",
                 "User-Agent": "DigitalMedia/1.0",
                 "x-opencode-session": "digitalmedia-transcricao-01"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["choices"][0]["message"]["content"]

if __name__ == "__main__":
    titulo = sys.argv[1] if len(sys.argv) > 1 else "episodio piloto"
    bruto = sys.argv[2] if len(sys.argv) > 2 else "bem gente hoje vou falar sobre trafego pago que e muito importante pra quem ta começando"
    key = load_key()
    if not key:
        print("ERRO: LLM_API_KEY nao encontrada em n8n/.env"); sys.exit(1)
    limpa = chat(key, MODEL_LIMPA,
        "Voce e o TRANSCRITOR DigitalMedia. Recebe transcricao bruta com erros. Entregue texto limpo PT-BR com pontuacao e paragrafos, sem cortar ideias, + 3 bullets resumo. Nao invente.",
        f"Titulo: {titulo}\nTexto bruto: {bruto}", 0.2)
    deriv = chat(key, MODEL_REDACAO,
        "Voce e o REDATOR DigitalMedia, nicho Marketing Digital. Tom direto, pratico, PT-BR, sem hype. A partir da transcricao limpa gere: H1 + artigo 400-600 palavras + 3 posts curtos + CTA. Sem promessa de ganho garantido.",
        f"Transcricao limpa:\n{limpa}", 0.7)
    out_dir = os.path.join("conteudo", "episodio-piloto")
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, "transcricao-limpa.md"), "w", encoding="utf-8").write(limpa)
    open(os.path.join(out_dir, "derivados.md"), "w", encoding="utf-8").write(deriv)
    print("OK salvo em " + out_dir + " | limpa chars=" + str(len(limpa)) + " derivados chars=" + str(len(deriv)))
