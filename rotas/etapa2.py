"""Aba 02: detalhes de uso (condições do cálculo e requisitos de cada software)."""
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
    if not (est["contratacao"] and est["finalidade"] and est["softwares"]):
        flash("Comece escolhendo o tipo de contratação e a finalidade.", "aviso")
        return redirect(url_for("etapa1.pagina"))

    if request.method == "POST":
        cond = {
            "multitarefa": request.form.get("multitarefa") if request.form.get("multitarefa") in
                           ("baixa", "moderada", "alta") else "moderada",
            "vida_util": parse_int(request.form.get("vida_util"), 5, 1, 15),
            "dados_locais_gb": (parse_int(request.form.get("dados_locais_gb"), 0, 0, 100000)
                                if request.form.get("dados_locais") else 0),
            "usuarios": parse_int(request.form.get("usuarios"), 1, 1, 1000),
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
            for comp in ("ram", "ssd", "cpu", "gpu"):
                if item["min"][comp] > item["rec"][comp]:
                    erros.append(f"{sid}: o mínimo de {comp.upper()} não pode ser maior que o recomendado.")
                    break

        est["cond"] = cond
        est["reqs_sw"] = novos
        if erros:
            flash("Em algum software o mínimo ficou maior que o recomendado. Corrija e salve de novo.", "erro")
            return render_template("etapa2.html", **_contexto(est))
        return redirect(url_for("resultado.pagina"))

    return render_template("etapa2.html", **_contexto(est))


def _contexto(est):
    return {
        "finalidade": FINALIDADES_POR_ID[est["finalidade"]],
        "softwares": softwares_do_estado(est),
        "cond": est["cond"],
        "gpu_rotulos": GPU_ROTULOS,
        "cpu_classes": list(range(CPU_MIN, CPU_MAX + 1)),
    }
