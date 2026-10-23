# -*- coding: utf-8 -*-
"""
verificar_integridade_audios.py
Verifica a existência e o tamanho mínimo dos arquivos MP3 das vozes neurais.
Se algum arquivo estiver ausente ou corrompido (< 50 KB), aciona a regeneração automática.
"""

import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

AUDIOS_OBRIGATORIOS = {
    "audiobook_habitos_noturnos.mp3": {
        "descricao": "Áudio Noturno (Voz: Antônio)",
        "tamanho_min_bytes": 100000 # 100 KB
    },
    "oracao_matinal_7min.mp3": {
        "descricao": "Clamor Matinal (Voz: Francisca)",
        "tamanho_min_bytes": 100000 # 100 KB
    }
}

def verificar():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    falhas = []

    print("=" * 65)
    print("[HEALTH-CHECK] VERIFICACAO DE INTEGRIDADE DOS AUDIOS NEURAIS")
    print("=" * 65)

    for nome_arquivo, info in AUDIOS_OBRIGATORIOS.items():
        caminho = os.path.join(AUDIO_DIR, nome_arquivo)
        if not os.path.exists(caminho):
            print(f"[ALERTA] Arquivo ausente: {nome_arquivo} ({info['descricao']})")
            falhas.append(nome_arquivo)
        else:
            tamanho = os.path.getsize(caminho)
            if tamanho < info["tamanho_min_bytes"]:
                print(f"[ALERTA] Arquivo corrompido ou incompleto: {nome_arquivo} ({tamanho} bytes)")
                falhas.append(nome_arquivo)
            else:
                print(f"[OK] {nome_arquivo}: Integro e protegido ({tamanho / 1024:.1f} KB)")

    if falhas:
        print(f"\n[AVISO] Detectada inconsistencia em {len(falhas)} arquivo(s). Iniciando auto-recuperacao...")
        script_gerador = os.path.join(SCRIPTS_DIR, "gerar_audios_neurais.py")
        cmd = [sys.executable, script_gerador]
        res = subprocess.run(cmd)
        if res.returncode == 0:
            print("[SUCESSO] Todos os audios foram regenerados e protegidos com sucesso!")
            return True
        else:
            print("[ERRO] Falha ao regenerar os arquivos de audio.")
            return False
    else:
        print("\n[OK] Todos os arquivos de voz neural estao 100% integros e salvos.")
        return True

if __name__ == "__main__":
    sucesso = verificar()
    sys.exit(0 if sucesso else 1)
