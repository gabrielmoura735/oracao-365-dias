# Plano de Implementação: Regravação do Clamor Matinal com Voz Diferente de Estúdio

Regravação do segundo áudio (**Oração e Clamor Matinal**) com o mesmo padrão de qualidade e cadência do primeiro áudio, utilizando uma voz diferente de alta fidelidade: a narradora **`pt-BR-FranciscaNeural`** (voz humana feminina, expressiva, serena e reverente).

---

## 1. O Que Será Alterado

### A. Nova Voz Neural para o Clamor Matinal (`oracao_matinal_7min.mp3`)
- **Voz Selecionada**: `pt-BR-FranciscaNeural`.
  - Proporciona o contraste perfeito:
    - 🎧 *Áudio Noturno (Áudio 1)*: Voz do Narrador **Antônio** (masculina, encorpada, calmante).
    - ⚡ *Clamor Matinal (Áudio 2)*: Voz da Narradora **Francisca** (feminina, inspiradora, cristalina e comovedora).
- **Ajuste de Cadência e Pausas**:
  - Aplicação de velocidade suave (`rate="-6%"`) e pausas respiratórias pontuadas, eliminando qualquer rigidez para soar 100% natural e humana, exatamente como o primeiro áudio.

### B. Atualização na Página `complementos/5_audio_reprogramacao_matinal.html`
- Atualização do player com o selo:  
  *`<i class="fa-solid fa-circle-check"></i> Narração Humana Neural de Estúdio • Voz: Francisca (Estúdio Brasil)`*.
- Inserção de parâmetro de versão no arquivo (`oracao_matinal_7min.mp3?v=2`) para evitar que o navegador toque o arquivo antigo guardado em cache.

### C. Publicação no GitHub
- Commitar e enviar o novo arquivo de áudio e a página atualizada para o repositório `gabrielmoura735/oracao-365-dias`.

---

## 2. Próximos Passos
- Obter sua aprovação.
- Executar o script de síntese neural e subir para o GitHub.
