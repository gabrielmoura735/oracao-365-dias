# Plano de Implementação: Blindagem e Proteção Permanente dos Áudios no GitHub

Implementação de um sistema de salvaguarda e redundância para garantir que os arquivos de áudio gravados com as vozes neurais de **Antônio** e **Francisca** nunca sejam perdidos, corrompidos ou sobrescritos durante atualizações automáticas ou alterações no repositório.

---

## 1. As 3 Camadas de Proteção que Serão Implementadas

### Camada 1: Blindagem da Esteira GitHub Actions (`.github/workflows/atualizacao_automatica.yml`)
- **Regra de Isolamento**: As rotinas automáticas de atualização diária e semanal ficam restritas exclusivamente à manipulação do feed de dados (`data/feed_atualizacao.json`), sem permissão de exclusão na pasta `audio/`.
- **Etapa de Verificação de Integridade (Audio Health-Check)**:
  - Antes de qualquer commit, a esteira confere se os arquivos `audiobook_habitos_noturnos.mp3` e `oracao_matinal_7min.mp3` existem e se possuem tamanho íntegro (> 100 KB).
  - Caso algum arquivo seja corrompido ou falte, a esteira executa automaticamente `scripts/gerar_audios_neurais.py` para regenerá-lo com as vozes exatas (Antônio e Francisca) antes de salvar.

### Camada 2: Backup Imutável via GitHub Releases (Nuvem Permanente)
- Criar uma **Release Oficial no GitHub** com a tag `v1.0-vozes-definitivas`.
- Fazer o upload dos dois arquivos MP3 como *Release Assets*.
- **Benefício**: Os arquivos ficam guardados nos servidores do GitHub de forma imutável. Mesmo que alguém delete a pasta localmente por engano, os áudios originais continuam salvos e acessíveis para sempre via link direto do GitHub.

### Camada 3: Script de Diagnóstico e Recuperação Local (`scripts/verificar_integridade_audios.py`)
- Script rápido para você rodar a qualquer momento no computador para checar o status, tamanho e integridade dos arquivos de voz.

---

## 2. Próximos Passos
- Obter sua aprovação.
- Atualizar a esteira do GitHub Actions, criar a Release oficial via GitHub CLI (`gh release create`) e publicar no repositório `gabrielmoura735/oracao-365-dias`.
