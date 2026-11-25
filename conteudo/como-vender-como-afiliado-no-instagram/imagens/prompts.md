# Prompts e Especificações — Como vender como afiliado no Instagram

**Projeto:** DigitalMedia  
**Pacote:** `conteudo/como-vender-como-afiliado-no-instagram/imagens/`  
**Data de produção:** 24/11/2026  
**Responsável:** CriadorImagens — DigitalMedia  
**Base documental:** `AGENTS.md`, `marca/voz-da-marca.md`, `brief.md`, `artigo-blog.md`, `social.md` e `roteiro-video.md`.

---

## Direção visual e pendências

- **Identidade aplicada (provisória):** ilustração vetorial/flat-3D editorial original, limpa e de alto contraste, com paleta provisória em **azul-escuro** (`#0B1F3A` / `#132E52` / `#14335C`), **amarelo** (`#FACC15`), **branco** (`#FFFFFF` / `#F8FAFC`) e apoios em **azul-ardósia** (`#24426B`).
- **[VERIFICAR]** tokens visuais oficiais da marca DigitalMedia (paleta definitiva, família tipográfica, grid e estilo ilustrativo). O `brief.md` não confirma tokens visuais; a paleta azul-escuro, amarelo e branco foi aplicada em caráter provisório de alto contraste.
- **Compliance visual aplicado em todas as 4 peças:**
  - Apenas ilustração original (sem bancos de imagens externos nem URLs simuladas).
  - Zero logos ou interfaces do Instagram, Meta, YouTube, plataformas de afiliação ou produtos de terceiros.
  - Zero pessoas reais identificáveis ou rostos.
  - Zero prints, dashboards, depoimentos, comprovantes, números de vendas, cifrões ou promessas de ganho/resultado.
  - Zero marca d'água.
  - Ortografia em PT-BR revisada visualmente em cada arquivo final; hero 100% sem texto; demais peças com texto exato em 2 linhas e leitura imediata em miniatura.

## Ferramentas, modelos e limitações gerais

- **Direção de arte:** especificada sob o perfil `CriadorImagens` (configuração de referência `opencode-go/mimo-v2.6-flash` no perfil do bot; sessão executada no agente Antigravity com modelo Gemini 4 Neon). Conforme catalogado no perfil do agente, o provedor `opencode-go` não disponibiliza modelo nativo de geração de imagens.
- **Geração de imagem:** ferramenta nativa `generate_image` executada via subagente nativo `image-generator` (o identificador exato do modelo de imagem subjacente não é exposto nos metadados da ferramenta `generate_image`).
- **Limitações técnicas da ferramenta nativa e pós-processamento:**
  1. A ferramenta `generate_image` gera arquivos apenas em `.jpg` e nas proporções fixas do gerador (`16:9` em `1376×768` e `3:4` em `896×1200`), sem opção direta de saída `.png`, proporção `4:5` nativa ou dimensões exatas em pixels (`1200×630`, `1080×1350`, `1280×720`).
  2. Para atender exatamente aos requisitos de formato e dimensões em pixels, os arquivos foram convertidos para PNG (`optimize=True`) e enquadrados com Python + Pillow 12.3.0 (`ImageOps.fit`, reamostragem `LANCZOS`, centralização `0.5, 0.5`).
  3. Todos os 4 PNGs finais foram inspecionados visualmente e validados programaticamente quanto a formato, integridade e dimensões exatas.

---

## 1. `hero-blog.png`

- **Arquivo:** `conteudo/como-vender-como-afiliado-no-instagram/imagens/hero-blog.png`
- **Dimensões finais:** `1200×630` px (PNG, ~1,91:1)
- **Texto na imagem:** Nenhum (verificado visualmente: zero palavras, letras ou números).
- **Ferramenta / modelo:** `image-generator` (`generate_image`, proporção nativa `16:9` em `1376×768` JPEG) + conversão e enquadramento exato para PNG `1200×630` via Python/Pillow (`LANCZOS`).
- **Alt text sugerido (SEO, alinhado ao `artigo-blog.md`):**  
  `Caderno e celular com um plano para quem quer aprender como vender como afiliado no Instagram, sem texto na imagem.`  
  *(Variante registrada no `brief.md`: "Caderno e celular com um plano de validação para afiliado no Instagram, sem texto na imagem.")*
- **Prompt utilizado:**
  > Ilustração editorial vetorial/flat-3D moderna com profundidade suave, iluminação direcional limpa e acabamento profissional de estúdio. Paleta provisória de alto contraste: fundo azul-escuro profundo (#0B1F3A com gradiente sutil para #132E52), elementos de destaque em amarelo vibrante (#FACC15) e superfícies limpas em branco (#F8FAFC) com detalhes em azul-ardósia (#24426B). Composição horizontal bem equilibrada em perspectiva levemente inclinada sobre superfície minimalista: um caderno aberto de capa azul-marinho e páginas brancas contendo apenas linhas e blocos geométricos abstratos em amarelo e azul; ao lado, um smartphone completamente abstrato e minimalista com blocos geométricos simples na tela (sem logos, sem ícones de Instagram/Meta, sem interface real); flutuando e organizados ao redor, três cartões de hipótese geométricos limpos (brancos com abas amarelas e símbolos geométricos abstratos: barras, seta simples e marca de seleção). Restrições absolutas: zero texto, zero letras, zero números, zero logos, zero marcas de terceiros, zero pessoas ou mãos, zero gráficos financeiros, zero dinheiro ou dashboards, zero marca d'água.
- **Limitações específicas:**
  - Origem gerada em `1376×768` (`16:9`) e ajustada por `ImageOps.fit` para `1200×630` (~6,6% de recorte vertical simétrico), preservando integralmente o caderno, o celular abstrato e os três cartões com margens confortáveis.
  - Paleta provisória aplicada; **[VERIFICAR]** tokens visuais oficiais da DigitalMedia antes da publicação definitiva.

---

## 2. `capa-carrossel.png`

- **Arquivo:** `conteudo/como-vender-como-afiliado-no-instagram/imagens/capa-carrossel.png`
- **Dimensões finais:** `1080×1350` px (PNG, 4:5)
- **Texto exato na imagem (2 linhas):**
  - Linha 1 (branco): `Valide antes`
  - Linha 2 (amarelo): `de vender`
- **Ferramenta / modelo:** `image-generator` (`generate_image`, proporção nativa `3:4` em `896×1200` JPEG) + conversão e enquadramento exato para PNG `1080×1350` via Python/Pillow (`LANCZOS`).
- **Alt text sugerido:**  
  `Capa de carrossel com a frase valide antes de vender.`
- **Prompt utilizado:**
  > Design editorial moderno de altíssimo contraste para capa de carrossel vertical, na mesma família visual em azul-escuro, amarelo e branco. Fundo azul-escuro profundo (#0B1F3A com gradiente radial sutil até #132E52), detalhes em azul-ardósia (#24426B), texto em branco puro (#FFFFFF) e amarelo vibrante (#FACC15). Na metade superior/central, texto grande, centralizado, fonte sans-serif geométrica extra-bold, altamente legível em miniatura, em exatamente duas linhas: linha 1 em branco "Valide antes" e linha 2 em amarelo vibrante "de vender". Abaixo do texto, uma única ideia visual limpa e centralizada: cartões de hipótese geométricos abstratos em branco e amarelo formando uma pequena pilha/sequência de validação, com símbolo geométrico simples de lupa com verificação (check) sobre o cartão em destaque e silhueta discreta de caderno, sem texto nos cartões. Margens amplas de segurança. Restrições absolutas: apenas o texto exato "Valide antes de vender", sem ponto final, sem subtítulo, zero outras letras ou números, zero logos/ícones do Instagram ou Meta, zero pessoas, zero dinheiro ou gráficos financeiros, zero marca d'água.
- **Limitações específicas:**
  - A ferramenta `generate_image` não oferece proporção `4:5` nativa; a peça foi gerada em `3:4` (`896×1200`) com margens amplas e ajustada para `1080×1350` (`4:5`) com recorte vertical simétrico (~6,25%) e reamostragem `LANCZOS` (~1,205× na largura).
  - Por ser texto rasterizado pelo modelo de imagem, edições futuras na tipografia exigem nova geração ou recriação em ferramenta vetorial/layout.
  - **[VERIFICAR]** tokens visuais oficiais da DigitalMedia.

---

## 3. `thumbnail-youtube-01.png`

- **Arquivo:** `conteudo/como-vender-como-afiliado-no-instagram/imagens/thumbnail-youtube-01.png`
- **Dimensões finais:** `1280×720` px (PNG, 16:9)
- **Texto exato na imagem (2 linhas):**
  - Linha 1 (branco): `Sem oferta?`
  - Linha 2 (amarelo): `Comece aqui`
- **Ferramenta / modelo:** `image-generator` (`generate_image`, proporção nativa `16:9` em `1376×768` JPEG) + conversão e redimensionamento exato para PNG `1280×720` via Python/Pillow (`LANCZOS`).
- **Alt text sugerido:**  
  `Thumbnail do vídeo com a frase sem oferta comece aqui.`
- **Prompt utilizado:**
  > Thumbnail editorial de YouTube 16:9 de altíssimo contraste com ilustração vetorial/flat-3D moderna e limpa, na mesma família visual em azul-escuro, amarelo e branco. Fundo azul-escuro profundo (#0B1F3A com iluminação sutil para #14335C), texto de impacto em branco puro (#FFFFFF) e amarelo vibrante (#FACC15). Composição em regra dos terços: lado esquerdo (~55%) com texto muito grande, alinhado à esquerda, fonte sans-serif extra-bold, leitura instantânea em miniatura, em exatamente duas linhas — linha 1 em branco "Sem oferta?" e linha 2 em amarelo vibrante "Comece aqui"; lado direito (~45%) com ilustração original limpa destacando um caderno minimalista azul-marinho/branco e um smartphone totalmente abstrato (sem marca nem interface real), com um cartão de hipótese branco iluminado por moldura amarela em primeiro plano e uma seta geométrica simples apontando para ele. Canto inferior direito desobstruído para o selo de duração do YouTube. Restrições absolutas: apenas o texto exato "Sem oferta? Comece aqui", zero outras palavras, letras ou números, zero rostos ou pessoas, zero logos/interfaces de terceiros, zero gráficos financeiros ou dinheiro, zero marca d'água.
- **Limitações específicas:**
  - Origem gerada em `1376×768` JPEG e convertida para PNG `1280×720` (`LANCZOS`, ajuste proporcional mínimo <0,8%).
  - Texto rasterizado no gerador; alterações futuras exigem nova geração ou edição em software de design.
  - **[VERIFICAR]** tokens visuais oficiais da DigitalMedia.

---

## 4. `thumbnail-youtube-02.png`

- **Arquivo:** `conteudo/como-vender-como-afiliado-no-instagram/imagens/thumbnail-youtube-02.png`
- **Dimensões finais:** `1280×720` px (PNG, 16:9)
- **Texto exato na imagem (2 linhas):**
  - Linha 1 (branco): `Antes de vender,`
  - Linha 2 (amarelo): `valide`
- **Ferramenta / modelo:** `image-generator` (`generate_image`, proporção nativa `16:9` em `1376×768` JPEG) + conversão e redimensionamento exato para PNG `1280×720` via Python/Pillow (`LANCZOS`).
- **Alt text sugerido:**  
  `Thumbnail do vídeo com a frase antes de vender valide.`
- **Prompt utilizado:**
  > Thumbnail editorial de YouTube 16:9 (variação B) na mesma família visual da variação A (ilustração vetorial/flat-3D editorial limpa em azul-escuro, amarelo e branco), com mudança de enquadramento e ênfase. Fundo azul-escuro profundo (#0B1F3A/#14335C), elementos secundários apagados em azul-ardósia (#24426B), destaque principal em amarelo vibrante (#FACC15) e branco puro (#FFFFFF). Lado esquerdo (~42%): ilustração original minimalista contrastando duas etapas abstratas — ao fundo, bloco e seta apagados em azul-acinzentado com ícone geométrico de pausa; à frente em destaque luminoso, seta curva amarela vibrante apontando para um cartão de hipótese branco limpo com ícone geométrico de check amarelo. Lado direito (~55%, mantendo respiro no canto inferior direito para o selo de duração do YouTube): texto muito grande, alinhado à esquerda, fonte sans-serif extra-bold, em exatamente duas linhas — linha 1 em branco "Antes de vender," e linha 2 bem grande e enfatizada em amarelo vibrante "valide". Restrições absolutas: apenas o texto exato "Antes de vender, valide" com vírgula após "vender", zero outras palavras, letras ou números, zero rostos ou pessoas, zero logos/interfaces de terceiros, zero gráficos financeiros ou dinheiro, zero marca d'água.
- **Limitações específicas:**
  - Origem gerada em `1376×768` JPEG (após iterações automáticas do subagente para precisão tipográfica e limpeza visual) e convertida para PNG `1280×720` (`LANCZOS`, ajuste proporcional mínimo <0,8%).
  - Texto rasterizado no gerador; alterações futuras exigem nova geração ou edição em software de design.
  - **[VERIFICAR]** tokens visuais oficiais da DigitalMedia.
