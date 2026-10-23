# Plano de Implementação: Automação Total do N8N (Instagram, YouTube, TikTok) + Inicializador CMD

Este plano detalha a criação do **Super Prompt de Orquestração** para o n8n e do **Script de Execução Automatizada via CMD** para rodar o n8n localmente no Windows com túnel HTTPS (essencial para a API do Instagram).

---

## 1. Diagnóstico do Ambiente do Sistema
- **Node.js**: Instalado (v26.x) e NPM pronto.
- **Docker**: Não detectado no sistema.
- **Solução Recomendada**: Execução direta via Node.js / NPX (`npx n8n --tunnel`), permitindo iniciar o n8n pelo CMD sem necessidade de instalar máquinas virtuais ou Docker, gerando automaticamente uma URL HTTPS pública válida para os Webhooks do Instagram/Meta.

---

## 2. Entregáveis Planejados

### A. Script de Automação para o CMD (`scripts/iniciar_n8n.bat`)
Criaremos um arquivo executável `.bat` para você rodar no CMD com um único comando ou clique:
1. **Configuração de Variáveis de Ambiente**:
   - `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=false` (evita conflitos de permissões no Windows).
   - `N8N_RUNNERS_ENABLED=true` (permite processamento veloz de tarefas em paralelo).
   - Habilitação do modo Túnel Seguro HTTPS para comunicação direta com a API do Instagram.
2. **Auto-inicialização**:
   - Inicia o n8n na porta `5678` e abre o navegador automaticamente em `http://localhost:5678`.
   - Gera o link do Webhook HTTPS público na tela do CMD.

### B. O Super Prompt de Configuração e Geração dos Workflows (Instagram + YouTube + TikTok)
Um prompt arquitetado especificamente para:
1. **Integração Central (Gatilho Único)**:
   - Recebe novo conteúdo (vídeo/áudio/imagem + texto + tags) via pasta local, Google Drive ou Webhook.
2. **Nó do Instagram (Graph API - Resolução do Passo Faltante)**:
   - Passo 1: Envio do arquivo para criar o *Media Container* (`POST /{ig-user-id}/media`).
   - Passo 2: Polling de espera com delay de 10 a 20s para garantir que o Instagram terminou de renderizar o Reel/Imagem.
   - Passo 3: Publicação final no feed/reels (`POST /{ig-user-id}/media_publish`).
3. **Nó do YouTube**:
   - Upload de vídeo/Short via YouTube Node oficial com tags, descrição e visibilidade pública.
4. **Nó do TikTok**:
   - Publicação direta via TikTok Content Posting API.
5. **Notificação de Sucesso/Erro**:
   - Envio de confirmação (com link dos posts publicados).

### C. Guia Rápido do Instagram Graph API
- Como pegar o `Instagram Account ID` e o `User Access Token` de 60 dias no Meta for Developers para desbloquear a última peça que falta.

---

## 3. Próximos Passos
Após sua aprovação:
1. Geraremos o arquivo `scripts/iniciar_n8n.bat` e testaremos os comandos do CMD.
2. Entregaremos o Super Prompt completo e estruturado para você colar diretamente no n8n / IA.
3. Forneceremos o JSON base importável do workflow caso queira importar com 1 clique no n8n.
