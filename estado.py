"""Guarda as respostas do usuário entre as abas.

Fica na memória do servidor (um espaço por visitante, identificado por cookie).
É suficiente para o MVP rodando no seu computador. Se um dia for para produção,
troque este arquivo por banco de dados mantendo as funções obter() e reiniciar().
"""
import copy
import uuid

from flask import session

from servicos.calculo import COND_PADRAO

_ARMAZEM = {}

PADRAO = {
    "contratacao": None,        # "licitacao" | "cotacao"
    "finalidade": None,         # id da finalidade
    "softwares": [],            # ids dos softwares marcados
    "reqs_sw": {},              # requisitos editados na etapa 2, por software
    "cond": dict(COND_PADRAO),  # multitarefa, vida útil, dados locais, usuários
    "nivel_spec": "alvo",       # licitação: "alvo" | "minimo"
    "precos": {"min": None, "rec": None, "fonte": "", "propostas": []},
    "estados": ["SC"],          # cotação
    "contatos": [],             # cotação: {empresa, data, resposta}
    "conferidos": {},           # cotação: id do ponto de busca -> data da conferência
}


def obter():
    sid = session.get("sid")
    if sid not in _ARMAZEM:
        sid = uuid.uuid4().hex
        session["sid"] = sid
        _ARMAZEM[sid] = copy.deepcopy(PADRAO)
    return _ARMAZEM[sid]


def reiniciar():
    sid = session.get("sid")
    if sid in _ARMAZEM:
        _ARMAZEM[sid] = copy.deepcopy(PADRAO)


def pronto_para_resultado(est):
    return bool(est["contratacao"] and est["finalidade"] and est["softwares"])
