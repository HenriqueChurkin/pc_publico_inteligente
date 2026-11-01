"""Cálculo da configuração mínima, alvo e recomendada.

Regra geral:
  1. Para cada componente, pega o MAIOR requisito entre os softwares escolhidos.
  2. Aplica as condições (multitarefa, vida útil, dados locais, usuários simultâneos).
  3. Alvo = média entre mínimo e recomendado (processador e vídeo são arredondados
     para cima, porque são classes inteiras).

Para mudar as regras de ajuste, edite a função calcular() abaixo.
"""
import math

from dados.componentes import (COMPONENTES, CPU_MAX, GPU_ROTULOS, RAM_PASSOS,
                               SSD_PASSOS)
from servicos.formatacao import formatar_componente

COND_PADRAO = {
    "multitarefa": "moderada",   # baixa | moderada | alta
    "vida_util": 5,              # anos
    "dados_locais_gb": 0,        # GB guardados no próprio computador
    "usuarios": 1,               # usuários simultâneos
}

IDS = ("ram", "ssd", "cpu", "gpu")


def _passo_acima(valor, passos):
    for p in passos:
        if p >= valor:
            return p
    return passos[-1]


def _subir(valor, passos, n=1):
    i = passos.index(_passo_acima(valor, passos))
    return passos[min(i + n, len(passos) - 1)]


def calcular(softwares, cond):
    """softwares: lista de {"nome", "fonte", "min": {...}, "rec": {...}}"""
    if not softwares:
        raise ValueError("Nenhum software selecionado.")

    cond = {**COND_PADRAO, **(cond or {})}
    ajustes = []

    mn = {c: max(s["min"][c] for s in softwares) for c in IDS}
    rc = {c: max(s["rec"][c] for s in softwares) for c in IDS}

    # 1) Multitarefa
    if cond["multitarefa"] == "alta":
        mn["ram"] = _subir(mn["ram"], RAM_PASSOS)
        rc["ram"] = _subir(rc["ram"], RAM_PASSOS)
        rc["cpu"] = min(rc["cpu"] + 1, CPU_MAX)
        ajustes.append("Multitarefa alta: memória RAM sobe um nível (mínimo e recomendado) "
                       "e o processador recomendado sobe uma classe.")

    # 2) Vida útil esperada
    vida = cond["vida_util"]
    if vida >= 8:
        mn["ram"] = _subir(mn["ram"], RAM_PASSOS)
        rc["ram"] = _subir(rc["ram"], RAM_PASSOS)
        rc["cpu"] = min(rc["cpu"] + 1, CPU_MAX)
        ajustes.append(f"Vida útil de {vida} anos: memória RAM sobe um nível (mínimo e recomendado) "
                       "e o processador recomendado sobe uma classe.")
    elif vida > 5:
        rc["ram"] = _subir(rc["ram"], RAM_PASSOS)
        rc["cpu"] = min(rc["cpu"] + 1, CPU_MAX)
        ajustes.append(f"Vida útil de {vida} anos: memória RAM e processador recomendados sobem um nível.")

    # 3) Usuários simultâneos
    usuarios = cond["usuarios"]
    if usuarios >= 5:
        mn["ram"] = _subir(mn["ram"], RAM_PASSOS)
        rc["ram"] = _subir(rc["ram"], RAM_PASSOS)
        ajustes.append(f"{usuarios} usuários simultâneos: memória RAM sobe um nível (mínimo e recomendado).")
    elif usuarios >= 2:
        rc["ram"] = _subir(rc["ram"], RAM_PASSOS)
        ajustes.append(f"{usuarios} usuários simultâneos: memória RAM recomendada sobe um nível.")

    # 4) Dados guardados localmente
    dados = cond["dados_locais_gb"]
    if dados > 0:
        mn["ssd"] = _passo_acima(mn["ssd"] + dados, SSD_PASSOS)
        rc["ssd"] = _passo_acima(rc["ssd"] + dados, SSD_PASSOS)
        ajustes.append(f"Dados locais de {dados} GB somados ao armazenamento (arredondado para o próximo tamanho comercial).")

    # Coerência: o recomendado nunca fica abaixo do mínimo
    for c in IDS:
        rc[c] = max(rc[c], mn[c])

    # Alvo
    alvo = {
        "ram": (mn["ram"] + rc["ram"]) / 2,
        "ssd": (mn["ssd"] + rc["ssd"]) / 2,
        "cpu": math.ceil((mn["cpu"] + rc["cpu"]) / 2),
        "gpu": math.ceil((mn["gpu"] + rc["gpu"]) / 2),
    }

    componentes = []
    for cid, nome in COMPONENTES:
        componentes.append({
            "id": cid,
            "nome": nome,
            "minimo": mn[cid],
            "alvo": alvo[cid],
            "recomendado": rc[cid],
            "min_txt": formatar_componente(cid, mn[cid]),
            "alvo_txt": formatar_componente(cid, alvo[cid]),
            "rec_txt": formatar_componente(cid, rc[cid]),
        })

    return {
        "componentes": componentes,
        "minimo": mn,
        "alvo": alvo,
        "recomendado": rc,
        "ajustes": ajustes,
        "cond": cond,
    }
