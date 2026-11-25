# Fábrica de Cortes — DigitalMedia

Cortes verticais 9:16 com legendas destacadas palavra por palavra, no estilo dos clips virais (TikTok/Reels/Shorts).

## Instalar (1 vez)

```powershell
pip install faster-whisper opencv-python numpy yt-dlp
```
Requer `ffmpeg` no PATH. GPU NVIDIA acelera a transcrição (detectada sozinha).

## Usar

```powershell
# Automático: encontra os 3 melhores momentos e corta
python cortar.py video.mp4 --auto 3

# De URL (YouTube etc.)
python cortar.py "https://..." --auto 5 --idioma pt

# Manual
python cortar.py video.mp4 --cortes "01:12-01:47,05:03-05:40"

# Sem seguimento de rosto (gameplay/tela cheia: crop central)
python cortar.py gameplay.mp4 --cortes "00:30-01:00" --sem-rosto --titulo gta-corte-1
```

Saída em `cortes/<titulo>/`: MP4 vertical 608×1080 com legenda queimada + `.srt` + `.ass`.

## Como funciona

1. **Transcrição** (`faster-whisper`, com VAD) com timestamps por palavra.
2. **Momentos** (`--auto`): pontua janelas de 25–55s por ganchos (perguntas, números, "como", "segredo", "erro"...) e pega os top N sem sobreposição.
3. **Vertical**: detecta o rosto (Haar cascade) e segue suavizado; sem rosto, crop central (`--sem-rosto` força).
4. **Legendas**: ASS karaokê (palavra atual em destaque) queimada via libass + normalização de áudio (`dynaudnorm`).
5. **Export**: H.264 + AAC com `faststart` (pronto p/ upload).

## Limites honestos

- Auto-detecção de "momento viral" é heurística — revise os cortes antes de postar.
- Rosto: Haar cascade erra com óculos escuros/perfil; gameplay usa `--sem-rosto`.
- Primeira execução baixa o modelo Whisper (~75 MB no `tiny`, ~500 MB no `small`).
