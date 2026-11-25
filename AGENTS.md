# DigitalMedia — Fábrica de Conteúdo

Projeto de bots para criação de conteúdo digital no nicho **Marketing Digital**.

## Equipe de bots (agentes)

Todos em `.opencode/agents/`:

| Bot | Arquivo | Função |
|-----|---------|--------|
| Orquestrador | `orquestrador.md` | Recebe o tema e coordena toda a equipe |
| Estrategista | `estrategista.md` | Pesquisa, pauta, palavra-chave, tendência, calendário |
| Redator Blog | `redator-blog.md` | Artigos SEO, guias, reviews |
| Social Media | `social-media.md` | Posts Instagram, TikTok, LinkedIn, X |
| Roteirista Vídeo | `roteirista-video.md` | Roteiros YouTube, Reels/TikTok, VSL |
| Copy Vendas | `copy-vendas.md` | Landing pages, e-mails, ofertas afiliado |
| Revisor | `revisor.md` | Revisão final, voz da marca, compliance |

## Como usar

1. **Via Orquestrador (recomendado):**
   ```
   Use o subagent orquestrador para criar conteúdo sobre "como vender como afiliado no Instagram"
   ```
   Ele vai acionar o resto da equipe e entregar o pacote completo em `conteudo/<tema>/`.

2. **Via bot direto:**
   ```
   Use o subagent redator-blog para escrever um artigo sobre "tráfego pago para iniciantes"
   Use o subagent social-media para criar 5 posts sobre "gatilhos mentais"
   Use o subagent roteirista-video para um roteiro YouTube sobre "funil de vendas"
   ```

3. **Via comandos rápidos:**
   - `/novo-conteudo` — pacote completo a partir de um tema
   - `/artigo-seo` — só artigo de blog
   - `/pack-social` — só pack redes sociais
   - `/roteiro-video` — só roteiro

## Pastas

- `conteudo/` — saída dos bots (um subpasta por tema)
- `marca/` — voz da marca, persona, ofertas
- `.opencode/agents/` — definição dos bots
- `.opencode/commands/` — atalhos

## Fluxo padrão

1. Estrategista → brief + keywords + ângulos
2. Redator / Social / Roteirista / Copy → produzem em paralelo
3. Revisor → revisa tudo antes de publicar
4. Arquivos salvos em `conteudo/<slug-do-tema>/`

Antes de publicar, revise sempre `revisor-checklist` em cada entrega.
