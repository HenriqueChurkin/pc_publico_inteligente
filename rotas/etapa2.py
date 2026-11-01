"""Aba 02: detalhes de uso."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

import estado
from dados.componentes import CPU_MAX, CPU_MIN, GPU_ROTULOS
from dados.finalidades import FINALIDADES_POR_ID
from servicos.formatacao import parse_int
from servicos.requisitos import softwares_do_estado

bp = Blueprint("etapa2", __name__)


@bp.route("/etapa2", methods=["GET", "POST"])
def pagina():
    est = estado.obter()
    if not (est.get("contratacao") and est.get("softwares")):
        flash("Comece escolhendo a finalidade do computador.", "aviso")
        return redirect(url_for("etapa1.pagina"))

    if request.method == "POST":
        # vida_util vem como valor de radio ("3", "5", "8")
        vida_raw = request.form.get("vida_util", "5")
        vida_map = {"3": 3, "5": 5, "8": 8}
        vida = vida_map.get(vida_raw, parse_int(vida_raw, 5, 1, 15))

        # usuarios vem como radio ("1", "2", "5")
        usuarios_raw = request.form.get("usuarios", "1")
        usuarios_map = {"1": 1, "2": 2, "5": 5}
        usuarios = usuarios_map.get(usuarios_raw, parse_int(usuarios_raw, 1, 1, 1000))

        cond = {
            "multitarefa": request.form.get("multitarefa") if request.form.get("multitarefa") in
                           ("baixa", "moderada", "alta") else "moderada",
            "vida_util": vida,
            "dados_locais_gb": parse_int(request.form.get("dados_locais_gb"), 0, 0, 100000),
            "usuarios": usuarios,
        }

        novos, erros = {}, []
        for sid in est["softwares"]:
            item = {"fonte": (request.form.get(f"{sid}__fonte") or "").strip() or "não informada",
                    "min": {}, "rec": {}}
            for tipo in ("min", "rec"):
                item[tipo] = {
                    "ram": parse_int(request.form.get(f"{sid}__{tipo}__ram"), 4, 1, 1024),
                    "ssd": parse_int(request.form.get(f"{sid}__{tipo}__ssd"), 128, 1, 100000),
                    "cpu": parse_int(request.form.get(f"{sid}__{tipo}__cpu"), CPU_MIN, CPU_MIN, CPU_MAX),
                    "gpu": parse_int(request.form.get(f"{sid}__{tipo}__gpu"), 0, 0, 3),
                }
            novos[sid] = item

        est["cond"] = cond
        est["reqs_sw"] = novos
        if erros:
            flash("Erro nos requisitos. Verifique e tente novamente.", "erro")
            return render_template("etapa2.html", **_contexto(est))
        return redirect(url_for("resultado.pagina"))

    return render_template("etapa2.html", **_contexto(est))


def _contexto(est):
    finalidade_id = (est.get("finalidades") or [est.get("finalidade")])[0]
    return {
        "finalidade": FINALIDADES_POR_ID.get(finalidade_id, {}),
        "softwares": softwares_do_estado(est),
        "cond": est["cond"],
        "gpu_rotulos": GPU_ROTULOS,
        "cpu_classes": list(range(CPU_MIN, CPU_MAX + 1)),
    }
