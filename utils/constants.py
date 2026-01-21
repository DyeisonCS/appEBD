"""
Constantes e dados mock para o Sistema EBD
"""
from datetime import date, timedelta
import random

# Configuracao da Igreja
CHURCH_NAME = "IPB Centro"
CHURCH_FULL_NAME = "Igreja Presbiteriana do Brasil - Centro"

# Versiculo motivacional
VERSE = '"Ensina a crianca no caminho em que deve andar, e, ainda quando for velho, nao se desviara dele." - Proverbios 22:6'

# Cores do tema
COLORS = {
    "primary": "#1E3A5F",
    "secondary": "#4A90D9",
    "accent": "#D4AF37",
    "background": "#F8F9FA",
    "text": "#333333",
    "success": "#28A745",
    "warning": "#FFC107",
    "danger": "#DC3545",
}

# Niveis de acesso
USER_ROLES = {
    "admin": "Administrador",
    "superintendent": "Superintendente",
    "teacher": "Professor",
}

# Classes EBD padrao IPB
CLASSES = [
    {"id": 1, "nome": "Bercario", "faixa_etaria": "0-2 anos", "idade_min": 0, "idade_max": 2, "icone": "👶"},
    {"id": 2, "nome": "Maternal", "faixa_etaria": "3-4 anos", "idade_min": 3, "idade_max": 4, "icone": "🧒"},
    {"id": 3, "nome": "Jardim de Infancia", "faixa_etaria": "5-6 anos", "idade_min": 5, "idade_max": 6, "icone": "🌻"},
    {"id": 4, "nome": "Primarios", "faixa_etaria": "7-8 anos", "idade_min": 7, "idade_max": 8, "icone": "📕"},
    {"id": 5, "nome": "Juniores", "faixa_etaria": "9-10 anos", "idade_min": 9, "idade_max": 10, "icone": "📗"},
    {"id": 6, "nome": "Pre-Adolescentes", "faixa_etaria": "11-12 anos", "idade_min": 11, "idade_max": 12, "icone": "📘"},
    {"id": 7, "nome": "Adolescentes", "faixa_etaria": "13-14 anos", "idade_min": 13, "idade_max": 14, "icone": "📙"},
    {"id": 8, "nome": "Juvenis", "faixa_etaria": "15-17 anos", "idade_min": 15, "idade_max": 17, "icone": "📒"},
    {"id": 9, "nome": "Jovens", "faixa_etaria": "18-35 anos", "idade_min": 18, "idade_max": 35, "icone": "📓"},
    {"id": 10, "nome": "Adultos", "faixa_etaria": "36+ anos", "idade_min": 36, "idade_max": 120, "icone": "📔"},
]

# Professores mock
PROFESSORES = [
    {"id": 1, "nome": "Maria Jose Silva", "classe_id": 1, "email": "maria.jose@email.com"},
    {"id": 2, "nome": "Pedro Santos", "classe_id": 2, "email": "pedro.santos@email.com"},
    {"id": 3, "nome": "Ana Costa", "classe_id": 3, "email": "ana.costa@email.com"},
    {"id": 4, "nome": "Lucas Souza", "classe_id": 4, "email": "lucas.souza@email.com"},
    {"id": 5, "nome": "Julia Lima", "classe_id": 5, "email": "julia.lima@email.com"},
    {"id": 6, "nome": "Marcos Rocha", "classe_id": 6, "email": "marcos.rocha@email.com"},
    {"id": 7, "nome": "Paula Santos", "classe_id": 7, "email": "paula.santos@email.com"},
    {"id": 8, "nome": "Rafael Dias", "classe_id": 8, "email": "rafael.dias@email.com"},
    {"id": 9, "nome": "Thiago Luz", "classe_id": 9, "email": "thiago.luz@email.com"},
    {"id": 10, "nome": "Rev. Carlos Oliveira", "classe_id": 10, "email": "rev.carlos@email.com"},
]

# Nomes para geracao de alunos mock
NOMES = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Hugo",
    "Isabela", "Joao", "Karen", "Leonardo", "Mariana", "Nicolas", "Olivia",
    "Pedro", "Quiteria", "Rafael", "Sofia", "Thiago", "Ursula", "Vinicius",
    "Wesley", "Ximena", "Yuri", "Zoe", "Amanda", "Bernardo", "Cecilia", "Diego",
    "Elena", "Fernando", "Giovana", "Henrique", "Iris", "Julio", "Katia", "Lucas",
    "Melissa", "Nathan", "Patricia", "Ricardo", "Sabrina", "Tomas", "Valentina"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves",
    "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho",
    "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha",
    "Dias", "Nascimento", "Andrade", "Moreira", "Nunes", "Marques", "Machado"
]


def gerar_alunos_mock():
    """Gera lista de alunos mock para todas as classes"""
    alunos = []
    aluno_id = 1

    for classe in CLASSES:
        # Quantidade de alunos por classe (variavel)
        qtd = random.randint(8, 25)

        for _ in range(qtd):
            # Calcula idade baseada na faixa etaria da classe
            idade = random.randint(classe["idade_min"], min(classe["idade_max"], 80))

            # Calcula data de nascimento aproximada
            hoje = date.today()
            ano_nasc = hoje.year - idade
            data_nasc = date(ano_nasc, random.randint(1, 12), random.randint(1, 28))

            aluno = {
                "id": aluno_id,
                "nome": f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}",
                "classe_id": classe["id"],
                "classe_nome": classe["nome"],
                "data_nascimento": data_nasc,
                "idade": idade,
                "telefone": f"({random.randint(11,99)}) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}",
                "email": f"aluno{aluno_id}@email.com" if idade >= 12 else None,
                "responsavel": f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}" if idade < 18 else None,
                "ativo": True,
            }
            alunos.append(aluno)
            aluno_id += 1

    return alunos


def gerar_chamadas_mock(alunos, semanas=8):
    """Gera historico de chamadas mock para as ultimas semanas"""
    chamadas = []
    hoje = date.today()

    # Encontra o ultimo domingo
    dias_desde_domingo = (hoje.weekday() + 1) % 7
    ultimo_domingo = hoje - timedelta(days=dias_desde_domingo)

    for semana in range(semanas):
        data = ultimo_domingo - timedelta(weeks=semana)

        for aluno in alunos:
            # Probabilidade de presenca (70-90%)
            presente = random.random() < random.uniform(0.70, 0.90)

            chamada = {
                "id": len(chamadas) + 1,
                "aluno_id": aluno["id"],
                "aluno_nome": aluno["nome"],
                "classe_id": aluno["classe_id"],
                "classe_nome": aluno["classe_nome"],
                "data": data,
                "presente": presente,
                "biblia": presente and random.random() < 0.85,
                "revista": presente and random.random() < 0.75,
                "oferta": round(random.uniform(0, 20), 2) if presente and random.random() < 0.60 else 0,
                "visitante": False,
            }
            chamadas.append(chamada)

    return chamadas


def calcular_estatisticas_classe(chamadas, classe_id, data=None):
    """Calcula estatisticas de uma classe para uma data especifica"""
    if data is None:
        data = date.today()

    chamadas_classe = [c for c in chamadas if c["classe_id"] == classe_id and c["data"] == data]

    if not chamadas_classe:
        return {
            "matriculados": 0,
            "presentes": 0,
            "frequencia": 0,
            "com_biblia": 0,
            "com_revista": 0,
            "total_ofertas": 0,
            "visitantes": 0,
        }

    presentes = sum(1 for c in chamadas_classe if c["presente"])
    total = len(chamadas_classe)

    return {
        "matriculados": total,
        "presentes": presentes,
        "frequencia": round((presentes / total) * 100, 1) if total > 0 else 0,
        "com_biblia": sum(1 for c in chamadas_classe if c["biblia"]),
        "com_revista": sum(1 for c in chamadas_classe if c["revista"]),
        "total_ofertas": sum(c["oferta"] for c in chamadas_classe),
        "visitantes": sum(1 for c in chamadas_classe if c["visitante"]),
    }


def calcular_estatisticas_gerais(chamadas, data=None):
    """Calcula estatisticas gerais de todas as classes"""
    if data is None:
        data = date.today()

    chamadas_data = [c for c in chamadas if c["data"] == data]

    if not chamadas_data:
        return {
            "total_matriculados": 0,
            "total_presentes": 0,
            "frequencia_geral": 0,
            "total_ofertas": 0,
            "total_visitantes": 0,
        }

    presentes = sum(1 for c in chamadas_data if c["presente"])
    total = len(chamadas_data)

    return {
        "total_matriculados": total,
        "total_presentes": presentes,
        "frequencia_geral": round((presentes / total) * 100, 1) if total > 0 else 0,
        "total_ofertas": sum(c["oferta"] for c in chamadas_data),
        "total_visitantes": sum(1 for c in chamadas_data if c["visitante"]),
    }


# Usuarios mock para login
USUARIOS_MOCK = [
    {
        "id": 1,
        "email": "admin@ipb.com",
        "senha": "admin123",
        "nome": "Administrador",
        "role": "admin",
        "classe_id": None,
    },
    {
        "id": 2,
        "email": "super@ipb.com",
        "senha": "super123",
        "nome": "Superintendente",
        "role": "superintendent",
        "classe_id": None,
    },
    {
        "id": 3,
        "email": "professor@ipb.com",
        "senha": "prof123",
        "nome": "Thiago Luz",
        "role": "teacher",
        "classe_id": 9,  # Jovens
    },
]


# Gerar dados mock ao importar
ALUNOS_MOCK = gerar_alunos_mock()
CHAMADAS_MOCK = gerar_chamadas_mock(ALUNOS_MOCK)
