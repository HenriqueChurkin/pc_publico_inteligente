"""Junta tudo que a tela de Resultado (e o relatório) precisam mostrar."""
from dados.estados import ESTADOS_POR_UF
from dados.finalidades import FINALIDADES_POR_ID
from servicos import fornecedores, precos, textos
from servicos.calculo import calcular
from servicos.requisitos import softwares_do_estado


def montar(est):
    finalidade = FINALIDADES_POR_ID[est["finalidade"]]
    sws = softwares_do_estado(est)
    calc = calcular(sws, est["cond"])

    ctx = {
        "contratacao": est["contratacao"],
        "finalidade": finalidade,
        "finalidade_nome": finalidade["nome"],
        "softwares": sws,
        "calc": calc,
        "cond": calc["cond"],
    }

    if est["contratacao"] == "licitacao":
        nivel = est["nivel_spec"]
        p = est["precos"]
        regua = None
        if p["min"] is not None and p["rec"] is not None:
            regua = precos.montar_regua(p["min"], p["rec"], p["propostas"])
        ctx.update({
            "nivel": nivel,
            "precos": {**p, "regua": regua},
            "regua": regua,
            "especificacao": textos.especificacao(calc, nivel),
        })
        ctx["justificativa"] = textos.justificativa({
            "finalidade_nome": finalidade["nome"], "softwares": sws, "calc": calc,
            "nivel": nivel, "precos": ctx["precos"],
        })
    else:
        ufs = est["estados"]
        ctx.update({
            "pedido": textos.pedido_orcamento(calc, finalidade["nome"]),
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
