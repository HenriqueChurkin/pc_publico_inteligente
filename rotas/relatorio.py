"""Exportar relatório: página limpa para imprimir ou salvar como PDF (Ctrl+P),
ou baixar como arquivo .html (acrescente ?baixar=1 na URL)."""
from flask import Blueprint, flash, make_response, redirect, render_template, request, url_for

import estado
from servicos import contexto

bp = Blueprint("relatorio", __name__)


@bp.route("/relatorio")
def pagina():
    est = estado.obter()
    if not estado.pronto_para_resultado(est):
        flash("Preencha as etapas 01 e 02 antes de exportar o relatório.", "aviso")
        return redirect(url_for("etapa1.pagina"))

    ctx = contexto.montar(est)
    resposta = make_response(render_template("relatorio.html", **ctx))
    if request.args.get("baixar"):
        resposta.headers["Content-Disposition"] = "attachment; filename=relatorio-pc-publico.html"
    return resposta
