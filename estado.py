"""Guarda as respostas do usuário entre as abas."""
import copy
import uuid

from flask import session
from servicos.calculo import COND_PADRAO

_ARMAZEM = {}

PADRAO = {
    "contratacao": None,
    "finalidade": None,
    "finalidades": [],
    "softwares": [],
    "reqs_sw": {},
    "cond": dict(COND_PADRAO),
    "precos": {"min": None, "rec": None, "fonte": "", "propostas": []},
    "estados": ["SC"],
    "contatos": [],
    "conferidos": {},
    "custom_sw": {},
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
    return bool(est.get("contratacao") and est.get("softwares"))
