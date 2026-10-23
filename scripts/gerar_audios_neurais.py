# -*- coding: utf-8 -*-
"""
gerar_audios_neurais.py
Gera arquivos MP3 de alta fidelidade usando vozes neurais humanas (pt-BR-AntonioNeural).
"""

import asyncio
import os
import edge_tts

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")

TEXTO_NOTURNO = """
Olá, seja muito bem-vindo ao áudio oficial de Hábitos Noturnos e Sono Blindado. 
Desacelere a sua respiração agora. Solte o peso dos seus ombros e sinta a paz invadir o seu quarto. 
Respire fundo, e enquanto o ar sai, entregue todas as preocupações e pendências deste dia nas mãos de Deus. 
O Salmo 4, versículo 8, nos ensina uma verdade inegociável: 'Em paz me deito e logo pego no sono, pois só Tu, Senhor, me fazes viver em segurança'. 
O sono não é fraqueza; o sono é um ato de profunda confiança no cuidado de Deus. 
Enquanto você repousa, o Todo-Poderoso continua trabalhando em favor da sua casa, dos seus projetos e do seu futuro. 
Nesta noite, desligue o ruído do mundo. Guarde o seu coração de toda cobrança e ansiedade. 
Que o Espírito Santo envolva este ambiente com uma blindagem impenetrável de serenidade. 
Nenhum mal te alcançará, e praga alguma chegará à sua tenda. 
Descanse com a certeza absoluta de que o amanhã trará novas misericórdias e grandes vitórias. 
Durma em perfeita paz, sob a proteção do Altíssimo.
"""

TEXTO_MATINAL = """
Seja bem-vindo à Oração de Autoridade e Reprogramação Matinal. 
Levante a sua cabeça, encha o peito de ar e tome posse da vida que Deus te presenteou nesta manhã! 
As Escrituras declaram que as misericórdias do Senhor se renovam a cada amanhecer. Grande é a Sua fidelidade! 
Senhor meu Deus e Pai Celestial, entro na Tua presença com ações de graças no coração e firme convicção em meus lábios. 
Consagro a Ti as primeiras horas deste novo dia. Consagro meus pensamentos, minhas decisões e cada passo que darei. 
Eu rejeito agora todo espírito de desânimo, preguiça, dúvida e medo. 
A Palavra de Deus garante em Segunda Timóteo 1:7 que Ele não nos deu espírito de covardia, mas de poder, amor e equilíbrio mental! 
Declaro a minha mente blindada contra toda distração e ruído deste mundo. 
Onde eu colocar a planta dos meus pés hoje, a graça e a sabedoria do Senhor se manifestarão. 
Abençoa o fruto do meu trabalho, guarda a minha família e abre portas de oportunidade que ninguém poderá fechar. 
Eu decreto que este dia será produtivo, abençoado e vitorioso em todas as áreas da minha vida. 
Em nome de Jesus, amém e amém!
"""

async def gerar_mp3(texto: str, voz: str, rate: str, destino: str):
    try:
        print(f"[AUDIO] Gerando {os.path.basename(destino)} com a voz {voz}...")
    except Exception:
        pass
    communicate = edge_tts.Communicate(texto.strip(), voice=voz, rate=rate)
    await communicate.save(destino)
    tamanho = os.path.getsize(destino)
    try:
        print(f"[OK] Arquivo gerado com sucesso: {os.path.basename(destino)} ({tamanho} bytes)")
    except Exception:
        pass

async def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    
    # 1. Áudio Noturno (Voz calma, ritmo mais lento para relaxar)
    noturno_path = os.path.join(AUDIO_DIR, "audiobook_habitos_noturnos.mp3")
    await gerar_mp3(TEXTO_NOTURNO, "pt-BR-AntonioNeural", "-10%", noturno_path)
    
    # 2. Áudio Matinal (Voz firme, ritmo natural enérgico de autoridade)
    matinal_path = os.path.join(AUDIO_DIR, "oracao_matinal_7min.mp3")
    await gerar_mp3(TEXTO_MATINAL, "pt-BR-AntonioNeural", "+0%", matinal_path)

if __name__ == "__main__":
    asyncio.run(main())
