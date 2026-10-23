# Plano de Implementação: Repositório Dedicado "vozes" e Humanização Vocal

Criação do repositório independente **`gabrielmoura735/vozes`**, estruturação do banco de vozes masculinas e femininas de alta fidelidade humana, inclusão de amostras reais em MP3 (eliminando qualquer sintetizador robótico do navegador) e integração pronta para importar em qualquer produto atual ou futuro.

---

## 1. Por Que as Vozes Pareciam Robotizadas e Como Vamos Corrigir

1. **Eliminação do Leitor do Navegador**: No teste do navegador, o botão estava acionando a síntese interna do sistema operacional (`window.speechSynthesis`), que utiliza vozes antigas e mecânicas da máquina.
2. **Motor de Humanização Acústica (Natural Audio Pipeline)**:
   - Todo áudio será gerado e reproduzido como **arquivo MP3 real**, processado com entonação humana, pausas de respiração e modulação harmônica de estúdio.
3. **Amostras Reais Pré-Gravadas**: Cada categoria de voz terá sua própria amostra de áudio MP3 real para você ouvir diretamente pelo player sem depender de sintetizador de navegador.
4. **Suporte a Links de Vozes Reais**: O repositório terá um módulo aberto para receber links externos de vozes reais (caso você queira nos mandar links de locutores, referências do YouTube, Drive ou ElevenLabs para integrarmos).

---

## 2. Estrutura do Novo Repositório `vozes`

Criar a pasta `c:\Users\User\Desktop\Projetos\vozes` e o repositório GitHub `gabrielmoura735/vozes`:

```
vozes/
├── README.md                           # Guia de como usar o repositório em qualquer produto
├── index.html                          # Catálogo & Player interativo online com áudios reais
├── scripts/
│   ├── motor_vozes.py                  # Script Python universal para gerar áudio em 1 clique
│   ├── humanizar_audio.py              # Filtro de equalização, calor acústico e pausas naturais
│   └── importar_vozes_externas.py      # Módulo para cadastrar links de vozes reais enviadas
├── data/
│   └── banco_vozes.json                # Catálogo das vozes masculinas e femininas por arquétipo
└── amostras/                           # Arquivos MP3 reais demonstrativos de alta fidelidade
    ├── voz_m_antonio_pastoral.mp3
    ├── voz_m_narrador_epico.mp3
    ├── voz_m_noturno_sereno.mp3
    ├── voz_f_francisca_clamor.mp3
    ├── voz_f_thalita_acolhedora.mp3
    └── voz_f_suave_paz.mp3
```

---

## 3. Como Você Irá Reutilizar Esse Repositório em Outros Projetos

Com o repositório `vozes` no GitHub, em qualquer novo projeto ou produto que você criar, basta clonar ou importar o módulo:
```python
from scripts.motor_vozes import gerar_audio_humanizado

gerar_audio_humanizado(
    texto="Seu texto do produto aqui",
    voz="antonio_pastoral", # ou qualquer voz do catálogo
    saida="meu_produto.mp3"
)
```

---

## 4. Próximos Passos
- Obter sua aprovação.
- Criar a pasta local `c:\Users\User\Desktop\Projetos\vozes`.
- Gerar as amostras reais em MP3, a interface do catálogo e o motor de humanização.
- Criar e subir o repositório no seu GitHub (`gabrielmoura735/vozes`).
- Se você tiver links de vozes reais que gostaria de adicionar como referência, pode enviar para incluirmos no banco!
