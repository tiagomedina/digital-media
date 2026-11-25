# Prompts e Metadados Visuais — Lançamento GTA VI

**Projeto:** DigitalMedia (`G:\Projetos\DigitalMedia`)  
**Pacote:** `conteudo/lancamento-gta-vi/imagens/`  
**Data de geração:** 24/11/2026  
**Paleta aplicada:** inspirada em GTA VI — violeta profundo (`#160B2F`), rosa (`#FF3D9A`), laranja (`#FF7A00`), ciano (`#1FD6C7`) e branco (`#FFFFFF`). A composição original foi preservada.

## Fluxo e ferramentas utilizadas

- **Direção de arte:** CriadorImagens (conforme `SOUL.md`, referência de direção `opencode-go/mimo-v2.6-flash`; sessão executada no agente Antigravity).
- **Geração original:** subagente nativo `image-generator` do agente (ferramenta `generate_image`). O provedor `opencode-go` não oferece modelo próprio de geração de imagem; a ferramenta `generate_image` não expõe no retorno o identificador interno do modelo subjacente.
- **Revisão de paleta (24/11/2026):** tratamento programático das quatro imagens aprovadas via Python/Pillow, sem nova geração por modelo. A paleta azul-escuro, amarelo e branco da DigitalMedia foi substituída por uma paleta inspirada em GTA VI, sem alterar composição, textos ou dimensões.
- **Limitação técnica registrada:** `generate_image` não aceita proporção `4:5` diretamente (mais próxima disponível: `3:4`, saída `896x1200`). Para `capa-carrossel.png`, foi aplicado recorte vertical centrado para proporção exata `4:5` e redimensionamento para `1080x1350`; a revisão de paleta preservou esse enquadramento.

---

## 1. `hero-blog.png`

- **Uso:** Hero editorial do artigo de blog (`artigo-blog.md`) — sem texto (o título vai no CMS).
- **Dimensões finais:** `1920 x 1080 px` (16:9, PNG; origem `1376 x 768 px` JPG).
- **Ferramenta / modelo:** `image-generator` (`generate_image`, `AspectRatio: 16:9`, modelo interno não exposto) + conversão/ajuste PNG e revisão de paleta via Pillow.
- **Alt text sugerido:** `Ilustração editorial noturna em violeta profundo, rosa, laranja e ciano de uma avenida costeira iluminada com palmeiras e horizonte urbano refletido na baía, com cartões abstratos de checklist e grade de calendário em primeiro plano.`
- **Prompt base da composição (geração original):**
  > Original mature editorial illustration for a digital media blog hero header about covering a major coastal-city open-world game launch without spoilers. Aspect ratio 16:9 widescreen. Scene: an elevated twilight-to-night view of a stylized modern coastal metropolis boulevard lined with silhouetted palm trees curving along a dark ocean bay, illuminated by warm golden-yellow streetlights and crisp white architectural highlights. In the subtle foreground, an abstract sleek editorial desk corner with glowing minimalist geometric checklist cards and calendar grid reflections (purely abstract geometric shapes, no text, no letters, no numbers). Strictly coherent high-contrast editorial palette of deep midnight navy blue (#0B1528, #13294B), vibrant editorial yellow (#FACC15, #FFD000), and crisp white (#FFFFFF) highlights. Sophisticated adult editorial illustration (modern magazine digital art style), crisp vector-painterly lighting, atmospheric depth, refined contrast. Negative constraints: absolutely no text, no words, no letters, no numbers, no watermarks, no Rockstar/PlayStation/Xbox logos, no recognizable characters or people's faces, no game screenshots, no weapons or violence, no recognizable game maps.

---

## 2. `capa-carrossel.png`

- **Uso:** Slide 1 (capa) do carrossel Instagram (`social.md`).
- **Texto renderizado (verificado):** `GTA VI` / `JÁ LANÇOU` / `SEM SPOILERS` (ortografia e acentuação em PT-BR conferidas visualmente: `JÁ` com acento agudo e `LANÇOU` com `Ç`).
- **Dimensões finais:** `1080 x 1350 px` (4:5, PNG; origem `896 x 1200 px` 3:4 JPG ajustada por recorte vertical centrado para 4:5).
- **Ferramenta / modelo:** `image-generator` (`generate_image`, `AspectRatio: 3:4`, modelo interno não exposto) + recorte 4:5, conversão PNG e revisão de paleta via Pillow.
- **Alt text sugerido:** `Capa editorial em violeta profundo, rosa, laranja e ciano com ícone de calendário confirmado no topo, título "GTA VI JÁ LANÇOU", selo "SEM SPOILERS" e silhueta noturna original de cidade litorânea com palmeiras refletidas na água.`
- **Prompt base da composição (geração original):**
  > High-contrast modern editorial typographic cover card for Instagram Slide 1 about the post-launch coverage of GTA VI without spoilers. Vertical portrait layout. Exact Portuguese text required with 100% accurate spelling and accents: main bold display headline (very large, uppercase, ultra-clean geometric sans-serif, high legibility on small mobile screens) "GTA VI" / "JÁ LANÇOU" (exact acute accent on Á and cedilla Ç); subtext pill badge cleanly centered below the headline: "SEM SPOILERS". Background: deep midnight navy blue (#0A1628 to #122645) with subtle editorial dot/calendar grid texture and clean geometric framing lines. Lower third: stylized original night coastal city skyline silhouette with palm trees and subtle glowing golden-yellow ocean horizon reflection. Accent graphics: a clean minimalist yellow checkmark/calendar verification badge icon near the top, crisp white and vibrant yellow (#FFD000 / #FACC15) contrast blocks. Negative constraints: no extra garbled or tiny unreadable text, no spelling mistakes in Portuguese, no watermarks, no Rockstar/PlayStation/Xbox logos, no official key art, game screenshots, maps, or characters.

---

## 3. `thumbnail-youtube-01.png`

- **Uso:** Opção 1 de thumbnail YouTube (`roteiro-video.md`).
- **Texto renderizado (verificado):** `GTA VI` / `SEM SPOILERS` (4 palavras, alto contraste para leitura em miniatura).
- **Dimensões finais:** `1280 x 720 px` (16:9, PNG; origem `1376 x 768 px` JPG).
- **Ferramenta / modelo:** `image-generator` (`generate_image`, `AspectRatio: 16:9`, modelo interno não exposto) + conversão/ajuste PNG e revisão de paleta via Pillow.
- **Alt text sugerido:** `Thumbnail de YouTube em violeta profundo, rosa, laranja e ciano com o texto grande "GTA VI SEM SPOILERS" à esquerda e um escudo luminoso com ícone de olho riscado sobre cartões editoriais e silhueta costeira noturna à direita.`
- **Prompt base da composição (geração original):**
  > Bold, scroll-stopping, ultra-legible 16:9 YouTube thumbnail designed to work even at tiny mobile miniature size. Exact Portuguese text required (4 words only, 100% accurate spelling, massive bold condensed/geometric uppercase sans-serif on the left ~60% of the frame): top line in crisp pure white (#FFFFFF) "GTA VI", bottom lines in vibrant yellow (#FFD000) with strong shadow "SEM SPOILERS". Right ~40% of the frame: a large, iconic, high-contrast editorial emblem — a sleek glowing yellow-and-white shield containing a bold crossed-out eye / spoiler-block verification icon, layered over an abstract dark-blue editorial card stack. Background: atmospheric deep midnight navy blue (#081426, #102544) with subtle stylized coastal night skyline silhouette, palm fronds, and dynamic golden-yellow light streaks. Palette: deep dark blue (#081426), bright high-contrast yellow (#FFD000), and crisp white (#FFFFFF). Negative constraints: only the exact words "GTA VI SEM SPOILERS", no extra small text, no misspelled letters, no watermarks, no Rockstar/PlayStation/Xbox logos, no game characters, screenshots, key art, or maps.

---

## 4. `thumbnail-youtube-02.png`

- **Uso:** Opção 2 de thumbnail YouTube (`roteiro-video.md`).
- **Texto renderizado (verificado):** `3 CHECAGENS` / `OFICIAIS` + numeração visual `01`, `02`, `03` nos cartões com ícones de visto (sem texto miúdo ilegível).
- **Dimensões finais:** `1280 x 720 px` (16:9, PNG; origem `1376 x 768 px` JPG).
- **Ferramenta / modelo:** `image-generator` (`generate_image`, `AspectRatio: 16:9`, modelo interno não exposto) + conversão/ajuste PNG e revisão de paleta via Pillow.
- **Alt text sugerido:** `Thumbnail de YouTube em violeta profundo, rosa, laranja e ciano com o texto em destaque "3 CHECAGENS OFICIAIS" à esquerda e três cartões editoriais inclinados numerados de 01 a 03 com sinais de verificação à direita.`
- **Prompt base da composição (geração original):**
  > Bold, high-contrast 16:9 YouTube thumbnail designed for instant readability in tiny mobile thumbnails, focused on a 3-step official fact-checking method. Exact Portuguese text required (3 words only, 100% accurate spelling, massive bold uppercase sans-serif on the left ~58% of the frame): prominent large numeral "3" and bold headline "3 CHECAGENS" in vibrant editorial yellow (#FFD000) and "OFICIAIS" in crisp pure white (#FFFFFF). Right ~42% of the frame: three sleek, angled dark-blue and white editorial verification cards stacked dynamically in depth, each featuring a large clean bold yellow checkmark icon and clean large badge numbers "01", "02", "03" with abstract horizontal line bars (no tiny unreadable text on the cards). Background: deep midnight navy blue (#081426 to #12284A) with subtle calendar-grid lines, soft coastal twilight palm silhouettes, and crisp yellow rim lighting. Palette: deep dark blue (#081426), bright editorial yellow (#FFD000), and crisp white (#FFFFFF). Negative constraints: exact Portuguese spelling "3 CHECAGENS OFICIAIS", no typos, no extra gibberish words, no watermarks, no Rockstar/PlayStation/Xbox logos, no game characters, screenshots, key art, or maps.

---

## Checklist de conformidade (verificado em 24/11/2026)

- [x] Todos os 4 arquivos PNG existem em `G:\Projetos\DigitalMedia\conteudo\lancamento-gta-vi\imagens\`, são válidos e não vazios.
- [x] Somente as 4 imagens solicitadas e este `prompts.md` foram salvos na pasta `imagens/`.
- [x] Zero spoilers, leaks, cenas de missões, finale ou enredo.
- [x] Nenhum key art, logotipo oficial, personagem, mapa, screenshot ou trecho de trailer da Rockstar, PlayStation ou Xbox.
- [x] Nenhuma marca d'água.
- [x] Ortografia e acentuação em PT-BR validadas visualmente em todas as peças com texto (`GTA VI JÁ LANÇOU` / `SEM SPOILERS`, `GTA VI SEM SPOILERS`, `3 CHECAGENS OFICIAIS`).
- [x] Paleta inspirada em GTA VI: violeta profundo, rosa, laranja e ciano, com branco de alto contraste.
- [x] Revisão de paleta aplicada sem alterar textos, composição ou dimensões.
- [x] Nenhuma URL de asset simulada.
