"""Monta a lista de softwares com os requisitos."""
import copy
from dados.finalidades import FINALIDADES_POR_ID
from dados.softwares import MANUAL, SOFTWARES


def _base(sid, custom_sw=None):
    if sid in SOFTWARES:
        return SOFTWARES[sid]
    if sid == "manual":
        return MANUAL
    # software customizado ("outra necessidade")
    nome = (custom_sw or {}).get(sid, sid[7:].replace("_", " ") if sid.startswith("custom_") else sid)
    sw = copy.deepcopy(MANUAL)
    sw["id"] = sid
    sw["nome"] = nome
    return sw


def requisitos_padrao(sid, custom_sw=None):
    b = _base(sid, custom_sw)
    return {"fonte": b["fonte"], "min": dict(b["min"]), "rec": dict(b["rec"])}


def softwares_do_estado(est):
    custom_sw = est.get("custom_sw", {})
    lista = []
    for sid in est.get("softwares", []):
        b = _base(sid, custom_sw)
        ed = est.get("reqs_sw", {}).get(sid) or requisitos_padrao(sid, custom_sw)
        lista.append({
            "id": sid,
            "nome": b["nome"],
            "fonte": ed["fonte"],
            "min": dict(ed["min"]),
            "rec": dict(ed["rec"]),
        })
    return lista


def softwares_padrao_da_finalidade(finalidade_id):
    """Softwares que já vêm marcados para a finalidade, com os requisitos originais.

    Usada na aba Conferir especificação quando não há uma consulta em andamento.
    """
    f = FINALIDADES_POR_ID[finalidade_id]
    ids = [sid for sid in f["padrao"] if sid in SOFTWARES] or ["manual"]
    lista = []
    for sid in ids:
        b = _base(sid)
        lista.append({"id": sid, "nome": b["nome"], "fonte": b["fonte"],
                      "min": copy.deepcopy(b["min"]), "rec": copy.deepcopy(b["rec"])})
    return lista
