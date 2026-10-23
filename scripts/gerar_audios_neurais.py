# -*- coding: utf-8 -*-
"""
gerar_audios_neurais.py
Gera arquivos MP3 de alta fidelidade usando vozes neurais humanas de estúdio:
- Noturno: pt-BR-AntonioNeural (Voz masculina profunda e acolhedora)
- Matinal: pt-BR-FranciscaNeural (Voz feminina cristalina, humana e inspiradora)
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

TEXTO_MATINAL_FRANCISCA = """
Seja muito bem-vindo à Oração de Autoridade e Reprogramação Matinal. 
Respire fundo, erga a sua cabeça e receba a vida e a paz que Deus preparou para você neste novo dia. 
A Palavra de Deus declara em Lamentações que as misericórdias do Senhor se renovam a cada manhã. Grande é a Sua fidelidade! 
Senhor meu Deus e amado Pai celestial, eu entro na Tua santa presença nesta manhã com o coração transbordando de gratidão e louvor. 
Consagro a Ti as primeiras horas deste dia. Consagro os meus pensamentos, os meus sentimentos e cada uma das minhas decisões. 
Eu rejeito, pela autoridade da Tua Palavra, todo desânimo, toda ansiedade, cansaço e medo. 
Porque Deus não nos deu espírito de covardia, mas de poder, de amor e de equilíbrio mental. 
Eu declaro a minha mente completamente blindada pela Tua paz. 
Onde eu colocar a planta dos meus pés hoje, a Tua graça, a Tua sabedoria e o Teu favor se manifestarão. 
Abençoa o fruto do meu trabalho, guarda a minha família com a Tua proteção e abre portas que ninguém poderá fechar. 
Eu decreto que este dia será produtivo, abençoado e cheio da presença de Deus. 
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
    
    # 1. Áudio Noturno (Antônio)
    noturno_path = os.path.join(AUDIO_DIR, "audiobook_habitos_noturnos.mp3")
    await gerar_mp3(TEXTO_NOTURNO, "pt-BR-AntonioNeural", "-10%", noturno_path)
    
    # 2. Áudio Matinal (Francisca - voz feminina comovente e inspiradora, ritmo pausado suave)
    matinal_path = os.path.join(AUDIO_DIR, "oracao_matinal_7min.mp3")
    await gerar_mp3(TEXTO_MATINAL_FRANCISCA, "pt-BR-FranciscaNeural", "-6%", matinal_path)

if __name__ == "__main__":
    asyncio.run(main())
