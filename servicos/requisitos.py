"""Monta a lista de softwares (com os requisitos, já editados pelo usuário, se houver)."""
import copy

from dados.finalidades import FINALIDADES_POR_ID
from dados.softwares import MANUAL, SOFTWARES


def _base(sid):
    return MANUAL if sid == "manual" else SOFTWARES[sid]


def requisitos_padrao(sid):
    b = _base(sid)
    return {"fonte": b["fonte"], "min": dict(b["min"]), "rec": dict(b["rec"])}


def softwares_do_estado(est):
    """Softwares escolhidos na etapa 1, com os requisitos da etapa 2."""
    lista = []
    for sid in est["softwares"]:
        b = _base(sid)
        ed = est["reqs_sw"].get(sid) or requisitos_padrao(sid)
        lista.append({
            "id": sid,
            "nome": b["nome"],
            "fonte": ed["fonte"],
            "min": dict(ed["min"]),
            "rec": dict(ed["rec"]),
        })
    return lista


def softwares_padrao_da_finalidade(finalidade_id):
    """Softwares que já vêm marcados para a finalidade, com requisitos originais."""
    f = FINALIDADES_POR_ID[finalidade_id]
    ids = f["padrao"] or ["manual"]
    lista = []
    for sid in ids:
        b = _base(sid)
        lista.append({"id": sid, "nome": b["nome"], "fonte": b["fonte"],
                      "min": copy.deepcopy(b["min"]), "rec": copy.deepcopy(b["rec"])})
    return lista
