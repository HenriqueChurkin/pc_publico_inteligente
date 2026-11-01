"""Aba: Conferir especificação já redigida (já existia no MVP).

O usuário cola o trecho de um edital; o programa compara com o cálculo e mostra
em gráfico, além de alertar sobre capacidade acima da referência e sobre marca,
modelo ou geração.
"""
from flask import Blueprint, jsonify, render_template, request

import estado
from dados.finalidades import FINALIDADES, FINALIDADES_POR_ID
from servicos import alertas
from servicos.calculo import COND_PADRAO, calcular
from servicos.requisitos import softwares_do_estado, softwares_padrao_da_finalidade

bp = Blueprint("conferir", __name__)

FINALIDADES_CONFERIR = [f for f in FINALIDADES if f["id"] != "outra"]


def _calculo_para(est, finalidade_id):
    """Se for a mesma finalidade da consulta em andamento, usa as escolhas do usuário."""
    if est["finalidade"] == finalidade_id and est["softwares"]:
        return calcular(softwares_do_estado(est), est["cond"]), True
    return calcular(softwares_padrao_da_finalidade(finalidade_id), COND_PADRAO), False


@bp.route("/conferir", methods=["GET", "POST"])
def pagina():
    est = estado.obter()
    padrao = est["finalidade"] if est["finalidade"] in {f["id"] for f in FINALIDADES_CONFERIR} else "projeto"

    if request.method == "GET":
        return render_template("conferir.html", finalidades=FINALIDADES_CONFERIR,
                               finalidade_sel=padrao, texto="", resultado=None)

    fid = request.form.get("finalidade")
    if fid not in FINALIDADES_POR_ID or fid == "outra":
        fid = padrao
    texto = request.form.get("texto", "")

    calc, usou_consulta = _calculo_para(est, fid)
    extraido = alertas.extrair_requisitos(texto)
    comparacao = alertas.comparar(extraido, calc)
    termos = alertas.detectar_termos(texto)

    # escala do gráfico de barras (RAM e SSD)
    graficos = []
    for linha in comparacao["linhas"]:
        comp = linha["comp"]
        if comp["id"] not in ("ram", "ssd"):
            continue
        valores = [comp["minimo"], comp["recomendado"]] + ([linha["valor"]] if linha["valor"] else [])
        topo = max(valores)
        graficos.append({
            "nome": comp["nome"],
            "barras": [
                {"rotulo": "Mínimo", "txt": comp["min_txt"], "pct": comp["minimo"] / topo * 100, "cls": "min"},
                {"rotulo": "Recomendado", "txt": comp["rec_txt"], "pct": comp["recomendado"] / topo * 100,
                 "cls": "rec"},
            ] + ([{"rotulo": "Texto do edital", "txt": linha["valor_txt"],
                   "pct": linha["valor"] / topo * 100, "cls": "texto " + linha["status"]}]
                 if linha["valor"] else []),
        })

    resultado = {
        "calc": calc, "linhas": comparacao["linhas"], "alertas_capacidade": comparacao["alertas"],
        "termos": termos, "graficos": graficos, "usou_consulta": usou_consulta,
        "rotulos": alertas.ROTULO_STATUS,
    }
    return render_template("conferir.html", finalidades=FINALIDADES_CONFERIR,
                           finalidade_sel=fid, texto=texto, resultado=resultado)


@bp.route("/conferir/termos", methods=["POST"])
def termos():
    """Usada pelo JavaScript para avisar na hora, enquanto o texto é digitado."""
    texto = (request.get_json(silent=True) or {}).get("texto", "")
    return jsonify(alertas.detectar_termos(texto))
