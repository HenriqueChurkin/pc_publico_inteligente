"""Aba: Início (mapa de conceito do fluxo)."""
from flask import Blueprint, redirect, render_template, url_for

import estado
from servicos.fornecedores import PRECO_NACIONAL, PRECOS_CONSULTA

bp = Blueprint("inicio", __name__)


@bp.route("/")
def pagina():
    return render_template("inicio.html", precos=PRECOS_CONSULTA, preco_nacional=PRECO_NACIONAL)


@bp.route("/reiniciar", methods=["POST"])
def reiniciar():
    estado.reiniciar()
    return redirect(url_for("etapa1.pagina"))
