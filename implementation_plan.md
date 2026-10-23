# Plano de Implementação: Automação Contínua no GitHub e Sincronização no Produto

Criação do repositório GitHub para o produto `365 Dias de Oração Poderosa`, implementação de esteira de automação (**GitHub Actions**) com agendamento diário e semanal (*cron*), e integração no produto web para que o aluno receba notificações e sincronize as novidades direto do GitHub.

---

## 1. Arquitetura da Automação no GitHub

### A. Repositório no GitHub (`gabrielmoura735/oracao-365-dias`)
- Inicializar Git localmente na pasta `NovoProjeto`.
- Conectar à conta já autenticada do GitHub (`gabrielmoura735`).
- Subir a Página de Vendas, os 5 Complementos, o Livro Digital e os scripts.
- Habilitar **GitHub Pages** para hospedar o produto online gratuitamente caso deseje.

### B. Esteira de Automação GitHub Actions (`.github/workflows/atualizacao_automatica.yml`)
- **Frequência Agendada**:
  - `cron: '0 3 * * *'` (executa todos os dias à meia-noite no horário de Brasília).
  - Suporte a execução manual com 1 clique (`workflow_dispatch`).
- **O que a automação faz no GitHub**:
  1. Executa o script `scripts/gerar_feed_diario.py`.
  2. Calcula o dia do ano (1 a 365) e a semana (1 a 52).
  3. Atualiza o arquivo `data/feed_atualizacao.json` com a oração do dia, o protocolo de jejum da semana, novos motivos de clamor e a versão atualizada da data.
  4. Realiza commit automático com mensagem: `[Auto-Update] Atualização Diária: Dia X liberado`.
  5. Faz push para o GitHub.

### C. Motor de Sincronização no Produto (`app_devocional_interativo.html`)
- Ao abrir o produto, o JavaScript faz um `fetch` leve no arquivo remoto do GitHub (`https://raw.githubusercontent.com/gabrielmoura735/oracao-365-dias/main/data/feed_atualizacao.json`).
- Se a versão da nuvem for mais recente que a versão salva no celular/computador do aluno:
  - Exibe banner animado no topo:  
    > 🔔 *"Nova Palavra, Oração e Protocolo de Jejum Liberados pelo Mentor! Clique para Atualizar seu Produto."*
  - Botão **"🔄 Sincronizar Agora"**: Baixa a nova oração, adiciona a nova folha no **Caderninho de Milagres** e avança a sequência de constância (*Streak*).

---

## 2. Arquivos que Serão Criados

1. `.github/workflows/atualizacao_automatica.yml`: Workflow do GitHub Actions para rodar a automação diária/semanal.
2. `scripts/gerar_feed_diario.py`: Script Python executado pelo GitHub Actions para gerar as atualizações.
3. `data/feed_atualizacao.json`: Arquivo de dados sincronizado que o produto consulta.
4. `app_devocional_interativo.html`: Central interativa do aluno com a automação de verificação e sincronização conectada ao GitHub.

---

## 3. Próximos Passos
- Aguardar sua aprovação.
- Criar os arquivos, inicializar o repositório git e publicar no GitHub da sua conta `gabrielmoura735`.
