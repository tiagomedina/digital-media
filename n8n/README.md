# n8n Local Docker — DigitalMedia

## 1. Preparar (só 1ª vez)
```powershell
cd G:\Projetos\DigitalMedia\n8n
copy .env.example .env
# edite .env e coloque sua OPENAI_API_KEY
```

## 2. Subir
```powershell
cd G:\Projetos\DigitalMedia\n8n
docker compose up -d
docker compose ps
docker compose logs -f n8n
```
Acesse: http://localhost:5678

## 3. Importar workflow
1. Abra http://localhost:5678 → crie conta local (1ª vez)
2. Workflows → ... → Import from File
3. Selecione `workflows/01-fabrica-conteudo.json`
4. Abra o workflow → ative (toggle Active no topo)
5. O node Webhook vai mostrar: `POST http://localhost:5678/webhook/fabrica`
   - Para teste com Test Workflow use a URL de teste que aparece no node.

## 4. Testar
```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:5678/webhook/fabrica -ContentType 'application/json' -Body '{"tema":"como vender como afiliado no Instagram","formatos":"blog,social,video","oferta":"curso afiliado"}'
```
Resposta = JSON com `brief, artigo, social, video, revisao`.

## 5. Comandos úteis
```powershell
docker compose logs n8n --tail 100
docker compose down
docker compose up -d --force-recreate
```

## Notas
- Workflow usa `{{$env.OPENAI_API_KEY}}` direto — sem criar Credential no n8n. Só precisa estar no `.env`.
- Custo médio por pacote completo (gpt-4o-mini): ~$0.05-0.15.
- Para publicar no WordPress/Instagram/Telegram, me peça o `02-publicacao.json`.
