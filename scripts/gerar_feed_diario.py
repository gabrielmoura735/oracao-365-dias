# -*- coding: utf-8 -*-
"""
gerar_feed_diario.py
Script executado automaticamente pelo GitHub Actions todos os dias ou semanas.
Calcula o dia do ano, semana e gera as mensagens do dia: Oração, Jejum e Caderninho.
"""

import json
import datetime
import os
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FEED_PATH = os.path.join(DATA_DIR, "feed_atualizacao.json")

# Temas recorrentes de oração e autoridade para os 365 dias
TEMAS_ORACOES = [
    ("Blindagem Espiritual & Proteção Familiar", "Salmo 91:1-2", "Senhor meu Deus, declaro neste dia que a Tua destra segura guarda a minha mente, minha saúde e minha família de todo laço oculto. Nenhum mal nos alcançará."),
    ("Quebra da Ansiedade & Paz Sobrenatural", "Filipenses 4:6-7", "Pai celestial, entrego toda sobrecarga e preocupação nas Tuas mãos. Que a Tua paz, que excede todo entendimento, governe o meu coração ao longo deste dia."),
    ("Clareza de Propósito & Sabedoria nas Decisões", "Tiago 1:5", "Espírito Santo, concede-me sabedoria divina e discernimento apurado para cada conversa, escolha e projeto que passará por minhas mãos hoje."),
    ("Prosperidade com Propósito & Trabalho Honrado", "Deuteronômio 28:8", "Declaro a bênção sobre o fruto do meu trabalho, a multiplicação dos meus recursos e o livramento de todo espírito de escassez e desperdício."),
    ("Domínio Próprio & Disciplina Inabalável", "2 Timóteo 1:7", "Deus não me deu espírito de covardia, mas de poder, amor e equilíbrio. Repreendo a procrastinação e consagro meu foco para cumprir minhas metas."),
    ("Cura das Emoções & Perdão Libertador", "Salmo 147:3", "Senhor, sara as feridas secretas e arranca toda raiz de mágoa. Escolho liberar perdão hoje para que a Tua graça flua sem impedimentos em meu caminho."),
    ("Gratidão e Celebração dos Milagres", "Salmo 103:1-2", "Bendize, ó minha alma, ao Senhor, e não te esqueças de nenhum dos Seus benefícios. Agradeço pelas portas abertas e pelos livramentos que nem cheguei a ver.")
]

# 52 Protocolos Semanais de Jejum
PROTOCOLOS_JEJUM = [
    ("Jejum de Daniel: Purificação & Clareza", "Abstenha-se de carnes vermelhas, doces e ultraprocessados durante 5 dias. Consuma legumes, frutas e água pura para desinflamar o corpo e afinar o espírito."),
    ("Jejum da Madrugada (05:00 às 06:00)", "Consagre a primeira hora do seu dia antes do nascer do sol. Apenas água ou chá sem açúcar até às 09:00 com foco em leitura bíblica ininterrupta."),
    ("Jejum Digital: Silenciamento das Redes", "Elimine o uso recreativo de redes sociais e notificações até o meio-dia por 7 dias. Dedique as pausas mentais para 3 minutos de intercessão."),
    ("Jejum Intermitente até o Meio-Dia", "Pule o café da manhã sólido. Beba 1 litro de água com limão e sal marinho entre 06:00 e 12:00, transformando o desconforto físico em busca espiritual."),
    ("Jejum de Palavras Negativas & Reclamação", "Desafio de 7 dias sem proferir nenhuma crítica, murmuração ou palavra de derrota. Sempre que sentir vontade de reclamar, declare uma bênção em voz alta.")
]

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    agora = datetime.datetime.now(datetime.timezone.utc)
    # Fuso horário de Brasília (UTC-3)
    brasilia_tz = datetime.timezone(datetime.timedelta(hours=-3))
    data_br = agora.astimezone(brasilia_tz)
    
    dia_ano = data_br.timetuple().tm_yday
    semana_ano = int(data_br.strftime("%U")) + 1
    dia_semana_nome = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"][data_br.weekday()]
    
    # Seleção dos temas
    tema_oracao = TEMAS_ORACOES[(dia_ano - 1) % len(TEMAS_ORACOES)]
    protocolo_jejum = PROTOCOLOS_JEJUM[(semana_ano - 1) % len(PROTOCOLOS_JEJUM)]
    
    versao_str = data_br.strftime("%Y%m%d%H")
    hash_versao = hashlib.md5(f"{dia_ano}-{semana_ano}-{versao_str}".encode()).hexdigest()[:8]
    
    feed = {
        "status": "online",
        "versao": f"v.{data_br.strftime('%Y.%m.%d')}-{hash_versao}",
        "data_formatada": data_br.strftime("%d/%m/%Y"),
        "dia_semana": dia_semana_nome,
        "dia_do_ano": dia_ano,
        "semana_do_ano": semana_ano,
        "ultima_atualizacao_utc": agora.isoformat(),
        
        "alerta_mentor": {
            "ativo": True,
            "titulo": f"Nova Palavra & Oração Liberadas para Hoje ({dia_semana_nome})",
            "mensagem": f"O Dia {dia_ano}/365 e o ciclo da Semana {semana_ano} foram atualizados no sistema. Sincronize para ver o direcionamento de hoje!",
            "tipo": "diario"
        },
        
        "oracao_do_dia": {
            "numero_dia": dia_ano,
            "titulo": tema_oracao[0],
            "versiculo_chave": tema_oracao[1],
            "clamor_texto": tema_oracao[2],
            "decreto_diario": f"Eu decreto que no meu Dia {dia_ano}, a paz de Deus governa meu lar e minhas decisões."
        },
        
        "jejum_da_semana": {
            "numero_semana": semana_ano,
            "titulo": protocolo_jejum[0],
            "instrucoes": protocolo_jejum[1],
            "meta_semanal": "Cumprir 3 dias da janela escolhida com hidratação rigorosa e oração ao meio-dia."
        },
        
        "caderninho_diario": {
            "dia": dia_ano,
            "pergunta_reflexao": "Pelo que você é grato a Deus antes mesmo deste dia começar?",
            "motivo_intercessao": "Ore por uma pessoa que te magoou ou por alguém da sua família que precisa de paz.",
            "registro_milagre_sugerido": "Anote qualquer resposta ou livramento observado nas últimas 24 horas."
        }
    }
    
    with open(FEED_PATH, "w", encoding="utf-8") as f:
        json.dump(feed, f, indent=2, ensure_ascii=False)
        
    try:
        print(f"[OK] Feed diario atualizado com sucesso!")
        print(f"  Dia {dia_ano}/365 | Semana {semana_ano}/52 | Versao: {feed['versao']}")
    except Exception:
        pass

if __name__ == "__main__":
    main()
