"""Aba 01: tipo de contratação e finalidade do computador."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

import estado
from dados.finalidades import FINALIDADES, FINALIDADES_POR_ID
from dados.softwares import SOFTWARES

bp = Blueprint("etapa1", __name__)


@bp.route("/etapa1", methods=["GET", "POST"])
def pagina():
    est = estado.obter()

    if request.method == "POST":
        contratacao = request.form.get("contratacao")
        finalidade = request.form.get("finalidade")
        marcados = request.form.getlist("softwares")

        erros = []
        if contratacao not in ("licitacao", "cotacao"):
            erros.append("Escolha o tipo de contratação.")
        if finalidade not in FINALIDADES_POR_ID:
            erros.append("Escolha a finalidade do computador.")
        else:
            validos = FINALIDADES_POR_ID[finalidade]["opcoes"]
            marcados = [s for s in marcados if s in validos]
            if finalidade == "outra":
                marcados = ["manual"]
            elif not marcados:
                erros.append("Marque ao menos um software da finalidade.")

        if erros:
            for e in erros:
                flash(e, "erro")
            # mantém o que o usuário já tinha escolhido na tela
            est["contratacao"] = contratacao if contratacao in ("licitacao", "cotacao") else est["contratacao"]
            return render_template("etapa1.html", **_contexto(est, finalidade, marcados))

        # se mudou a finalidade, descarta os requisitos editados antes
        if finalidade != est["finalidade"]:
            est["reqs_sw"] = {}
        est["reqs_sw"] = {k: v for k, v in est["reqs_sw"].items() if k in marcados}
        est["contratacao"] = contratacao
        est["finalidade"] = finalidade
        est["softwares"] = marcados
        return redirect(url_for("etapa2.pagina"))

    return render_template("etapa1.html", **_contexto(est, est["finalidade"], est["softwares"]))


def _contexto(est, finalidade, marcados):
    # dados enviados ao JavaScript para trocar a lista de softwares sem recarregar a página
    dados_js = {
        f["id"]: {
            "padrao": f["padrao"],
            "opcoes": [{"id": s, "nome": SOFTWARES[s]["nome"], "fonte": SOFTWARES[s]["fonte"]}
                       for s in f["opcoes"]],
        }
        for f in FINALIDADES
    }
    return {
        "finalidades": FINALIDADES,
        "finalidade_sel": finalidade,
        "softwares_sel": marcados,
        "dados_js": dados_js,
    }
