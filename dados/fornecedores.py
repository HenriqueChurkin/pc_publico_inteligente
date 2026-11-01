"""Pontos de busca de fornecedores.

Enquanto um estado NÃO estiver em CURADOS, o programa gera nomes genéricos
("Loja Exemplo A") para não afirmar que consultou fontes que não consultou.

Para cadastrar nomes reais, depois de conferidos pela equipe, preencha CURADOS assim:

CURADOS = {
    "SC": {
        "distribuidores": [
            {"nome": "Nome real da empresa", "local": "Florianópolis",
             "atende_pj": "sim",               # "sim", "não" ou "a confirmar"
             "ultima_conferencia": "2026-10-15"},  # AAAA-MM-DD
        ],
        "revendas": [],
        "varejistas": [],
        "online": [],
    },
}
"""

CATEGORIAS = [
    ("distribuidores", "Distribuidores de TI"),
    ("online", "Lojas online"),
    ("revendas", "Revendas regionais"),
    ("varejistas", "Varejistas de eletrônicos com atendimento a empresas"),
]

CURADOS = {}
