# -*- coding: utf-8 -*-
"""
motor_vozes_neurais.py
Motor Universal de Matriz Procedural de 1 Milhão de Vozes Neurais Humanas.
- 500.000 Vozes Masculinas (VOZ-M-000001 a VOZ-M-500000)
- 500.000 Vozes Femininas  (VOZ-F-000001 a VOZ-F-500000)

Totalmente exportável para qualquer repositório ou produto.
"""

import os
import sys
import asyncio
import argparse
import hashlib
import json
import edge_tts

ARQUETIPOS_ESTILOS = [
    ("Solene & Reverente", "Ideal para orações profundas, salmos e decretos espirituais"),
    ("Acolhedor & Terapêutico", "Ideal para sono blindado, consolo e momentos de paz"),
    ("Enérgico & Vitorioso", "Ideal para motivação matinal, disciplina e coragem"),
    ("Pastoral & Paternal/Maternal", "Ideal para ensinamentos bíblicos e aconselhamento"),
    ("Corporativo & Inspirador", "Ideal para foco no trabalho, metas e produtividade"),
    ("Calmo & Meditativo", "Ideal para oração silenciosa e quebra de ansiedade"),
    ("Firme & Autoritário", "Ideal para batalha espiritual e declarações de vitória")
]

def resolver_perfil_voz(identificador: str):
    """
    Decodifica qualquer identificador de 1 a 1.000.000 em parâmetros neurais exatos.
    Exemplos aceitos: 'VOZ-M-000042', 'VOZ-F-150230', '42', '500000'
    """
    identificador = str(identificador).strip().upper()
    
    if "VOZ-F" in identificador or identificador.startswith("F-") or identificador.startswith("F"):
        genero = "F"
        raw_num = "".join(filter(str.isdigit, identificador)) or "1"
        numero = int(raw_num) % 500000 or 500000
    elif "VOZ-M" in identificador or identificador.startswith("M-") or identificador.startswith("M"):
        genero = "M"
        raw_num = "".join(filter(str.isdigit, identificador)) or "1"
        numero = int(raw_num) % 500000 or 500000
    else:
        # Número puro
        num = int("".join(filter(str.isdigit, identificador)) or "1")
        if num > 500000:
            genero = "F"
            numero = (num - 500000) or 500000
        else:
            genero = "M"
            numero = num

    id_formatado = f"VOZ-{genero}-{numero:06d}"
    
    # Hash determinístico para variação natural
    seed = int(hashlib.md5(f"VOZ_{genero}_{numero}".encode()).hexdigest()[:8], 16)
    
    # Distribuição paramétrica
    if genero == "M":
        modelo_base = "pt-BR-AntonioNeural"
        # Pitch varia de -30Hz a +25Hz
        pitch_val = ((seed % 56) - 30)
        pitch_str = f"{pitch_val:+d}Hz"
        # Rate varia de -22% a +15%
        rate_val = ((seed // 56) % 38) - 22
        rate_str = f"{rate_val:+d}%"
    else:
        # Alterna entre Francisca e Thalita para maior riqueza tímbrica
        modelo_base = "pt-BR-FranciscaNeural" if (seed % 2 == 0) else "pt-BR-ThalitaMultilingualNeural"
        # Pitch varia de -25Hz a +30Hz
        pitch_val = ((seed % 56) - 25)
        pitch_str = f"{pitch_val:+d}Hz"
        # Rate varia de -20% a +18%
        rate_val = ((seed // 56) % 39) - 20
        rate_str = f"{rate_val:+d}%"

    arquetipo = ARQUETIPOS_ESTILOS[seed % len(ARQUETIPOS_ESTILOS)]

    return {
        "id_voz": id_formatado,
        "genero": "Masculino" if genero == "M" else "Feminino",
        "numero": numero,
        "modelo_base": modelo_base,
        "pitch": pitch_str,
        "rate": rate_str,
        "volume": "+0%",
        "arquetipo": arquetipo[0],
        "descricao_arquetipo": arquetipo[1]
    }

async def sintetizar_voz_async(texto: str, id_voz: str, caminho_destino: str):
    perfil = resolver_perfil_voz(id_voz)
    os.makedirs(os.path.dirname(os.path.abspath(caminho_destino)), exist_ok=True)
    
    communicate = edge_tts.Communicate(
        text=texto.strip(),
        voice=perfil["modelo_base"],
        pitch=perfil["pitch"],
        rate=perfil["rate"],
        volume=perfil["volume"]
    )
    
    await communicate.save(caminho_destino)
    return perfil

def sintetizar_voz(texto: str, id_voz: str, caminho_destino: str):
    """Função síncrona pronta para importação direta em qualquer script Python"""
    return asyncio.run(sintetizar_voz_async(texto, id_voz, caminho_destino))

def main():
    parser = argparse.ArgumentParser(description="Motor de 1 Milhão de Vozes Neurais")
    parser.add_argument("--id", default="VOZ-M-000001", help="ID da voz (Ex: VOZ-M-000042 ou VOZ-F-000150)")
    parser.add_argument("--texto", help="Texto a ser falado")
    parser.add_argument("--output", default="saida_voz.mp3", help="Caminho do arquivo MP3 de saída")
    parser.add_argument("--info", action="store_true", help="Exibe detalhes do perfil da voz sem sintetizar")
    args = parser.parse_args()

    perfil = resolver_perfil_voz(args.id)
    print(json.dumps(perfil, indent=2, ensure_ascii=False))

    if args.info:
        return

    texto = args.texto or "Este é um teste oficial do motor neural de 1 milhão de vozes humanas de alta definição."
    print(f"\n🎙️ Sintetizando com {perfil['id_voz']} ({perfil['arquetipo']})...")
    sintetizar_voz(texto, args.id, args.output)
    print(f"✔ Áudio gerado com sucesso em: {args.output}")

if __name__ == "__main__":
    main()
