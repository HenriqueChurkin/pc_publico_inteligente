"""Abas do menu superior, na ordem em que aparecem.

Para criar uma aba nova: crie o arquivo em rotas/, registre em app.py e acrescente aqui.
  blueprint = nome do blueprint | endpoint = nome da função da rota
"""

ABAS = [
    {"blueprint": "inicio",    "endpoint": "inicio.pagina",    "numero": "",   "rotulo": "Início"},
    {"blueprint": "etapa1",    "endpoint": "etapa1.pagina",    "numero": "01", "rotulo": "Tipo e finalidade"},
    {"blueprint": "etapa2",    "endpoint": "etapa2.pagina",    "numero": "02", "rotulo": "Detalhes de uso"},
    {"blueprint": "resultado", "endpoint": "resultado.pagina", "numero": "03", "rotulo": "Resultado"},
    {"blueprint": "conferir",  "endpoint": "conferir.pagina",  "numero": "",   "rotulo": "Conferir especificação"},
]
