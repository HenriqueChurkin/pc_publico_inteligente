"""Aba 01: tipo de contratação e finalidade(s) do computador."""
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
        finalidades_sel = request.form.getlist("finalidade")
        marcados = request.form.getlist("softwares")

        erros = []
        if contratacao not in ("licitacao", "cotacao"):
            erros.append("Escolha como a compra será feita.")
        if not finalidades_sel:
            erros.append("Escolha ao menos uma finalidade para o computador.")
        else:
            finalidades_sel = [f for f in finalidades_sel if f in FINALIDADES_POR_ID]
            if not finalidades_sel:
                erros.append("Finalidade inválida.")

        if erros:
            for e in erros:
                flash(e, "erro")
            est["contratacao"] = contratacao if contratacao in ("licitacao", "cotacao") else est["contratacao"]
            return render_template("etapa1.html", **_contexto(est, finalidades_sel, marcados))

        tem_outra = "outra" in finalidades_sel
        tem_normal = any(f != "outra" for f in finalidades_sel)

        if tem_outra and not tem_normal:
            # só "outra" — pega chips customizados
            custom = [s for s in marcados if s.startswith("custom_")]
            # cria softwares dinâmicos no estado
            est["custom_sw"] = {}
            for s in custom:
                nome_chave = "custom_nome_" + s
                nome = request.form.get(nome_chave, s[7:].replace("_", " ")).strip()
                est["custom_sw"][s] = nome
            marcados = custom if custom else ["manual"]
        else:
            todos_validos = set()
            for fid in finalidades_sel:
                if fid != "outra":
                    todos_validos.update(FINALIDADES_POR_ID[fid]["opcoes"])
            marcados = [s for s in marcados if s in todos_validos and s in SOFTWARES]
            if not marcados:
                padrao = set()
                for fid in finalidades_sel:
                    if fid != "outra":
                        padrao.update(FINALIDADES_POR_ID[fid]["padrao"])
                marcados = [s for s in padrao if s in SOFTWARES]

        if set(finalidades_sel) != set(est.get("finalidades", [])):
            est["reqs_sw"] = {}
        est["reqs_sw"] = {k: v for k, v in est["reqs_sw"].items() if k in marcados}
        est["contratacao"] = contratacao
        est["finalidade"] = finalidades_sel[0]
        est["finalidades"] = finalidades_sel
        est["softwares"] = marcados
        return redirect(url_for("etapa2.pagina"))

    finalidades_atuais = est.get("finalidades") or ([est["finalidade"]] if est.get("finalidade") else [])
    return render_template("etapa1.html", **_contexto(est, finalidades_atuais, est["softwares"]))


def _contexto(est, finalidades_sel, marcados):
    dados_js = {}
    for f in FINALIDADES:
        dados_js[f["id"]] = {
            "padrao": f["padrao"],
            "opcoes": [
                {"id": s, "nome": SOFTWARES[s]["nome"]}
                for s in f["opcoes"] if s in SOFTWARES
            ],
        }
    return {
        "est": est,
        "finalidades": FINALIDADES,
        "finalidades_sel": finalidades_sel or [],
        "softwares_sel": marcados or [],
        "dados_js": dados_js,
    }
