"""Monta o contexto para a tela de resultado."""
from dados.componentes import faixa_preco, preco_config
from dados.estados import ESTADOS_POR_UF
from dados.finalidades import FINALIDADES_POR_ID
from servicos import fornecedores, precos, textos
from servicos.calculo import calcular
from servicos.requisitos import softwares_do_estado


def montar(est):
    finalidades_ids = est.get("finalidades") or ([est["finalidade"]] if est.get("finalidade") else [])
    finalidade = FINALIDADES_POR_ID[finalidades_ids[0]]
    finalidades_nomes = [FINALIDADES_POR_ID[fid]["nome"] for fid in finalidades_ids]

    sws = softwares_do_estado(est)
    calc = calcular(sws, est["cond"])

    # Preços automáticos baseados nos componentes calculados
    p_min, p_rec, variacao = faixa_preco(calc)
    faixa_auto = {
        "preco_min": p_min,
        "preco_rec": p_rec,
        "variacao": variacao,
        "min_baixo": int(p_min * (1 - variacao)),
        "min_alto":  int(p_min * (1 + variacao)),
        "rec_baixo": int(p_rec * (1 - variacao)),
        "rec_alto":  int(p_rec * (1 + variacao)),
    }

    ctx = {
        "contratacao": est["contratacao"],
        "finalidade": finalidade,
        "finalidade_nome": " + ".join(finalidades_nomes),
        "finalidades_nomes": finalidades_nomes,
        "softwares": sws,
        "calc": calc,
        "cond": calc["cond"],
        "faixa_auto": faixa_auto,
    }

    if est["contratacao"] == "licitacao":
        p = est["precos"]
        regua = None
        if p["min"] is not None and p["rec"] is not None:
            regua = precos.montar_regua(p["min"], p["rec"], p["propostas"])
        ctx_precos = {**p, "regua": regua}
        # Gera os dois textos para troca dinâmica via JS
        ctx.update({
            "precos": ctx_precos,
            "regua": regua,
            "especificacao_min": textos.especificacao(calc, "minimo"),
            "especificacao_rec": textos.especificacao(calc, "recomendado"),
            "justificativa_min": textos.justificativa({
                "finalidade_nome": ctx["finalidade_nome"], "softwares": sws, "calc": calc,
                "nivel": "minimo", "precos": ctx_precos,
            }),
            "justificativa_rec": textos.justificativa({
                "finalidade_nome": ctx["finalidade_nome"], "softwares": sws, "calc": calc,
                "nivel": "recomendado", "precos": ctx_precos,
            }),
        })
    else:
        ufs = est["estados"]
        ctx.update({
            "pedido": textos.pedido_orcamento(calc, ctx["finalidade_nome"]),
            "estados_sel": [ESTADOS_POR_UF[u] for u in ufs],
            "pontos": [
                {"uf": u, "nome": ESTADOS_POR_UF[u][1],
                 "categorias": fornecedores.pontos_de_busca(u, est["conferidos"])}
                for u in ufs
            ],
            "contatos": est["contatos"],
            "valor_consulta": fornecedores.preco_consulta(len(ufs)),
        })
    return ctx
