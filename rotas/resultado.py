"""Aba 03: resultado. A tela muda conforme o tipo de contratação.

  Licitação pública -> configuração mínima ou recomendada, preços, especificação, justificativa e comparação de propostas
  Cotação           -> estados, texto do pedido de orçamento, registro de contatos, pontos de busca

As rotas POST abaixo salvam o que o usuário digitou e voltam para a mesma tela.
"""
from flask import Blueprint, flash, redirect, render_template, request, url_for

import estado
from dados.estados import ESTADOS, ESTADOS_POR_UF
from servicos import contexto
from servicos.formatacao import hoje_iso, parse_brl

bp = Blueprint("resultado", __name__)

RESPOSTAS = ["Aguardando", "Respondeu", "Sem resposta", "Não atende pessoa jurídica"]


def _voltar(ancora=""):
    return redirect(url_for("resultado.pagina") + (f"#{ancora}" if ancora else ""))


@bp.route("/resultado")
def pagina():
    est = estado.obter()
    if not estado.pronto_para_resultado(est):
        flash("Preencha as etapas 01 e 02 para ver o resultado.", "aviso")
        return redirect(url_for("etapa1.pagina"))

    ctx = contexto.montar(est)
    if est["contratacao"] == "licitacao":
        return render_template("resultado_licitacao.html", **ctx)
    return render_template("resultado_cotacao.html", estados=ESTADOS, respostas=RESPOSTAS, **ctx)


# --------------------------------------------------------------------------- licitação
@bp.route("/resultado/precos", methods=["POST"])
def precos():
    est = estado.obter()
    pmin = parse_brl(request.form.get("preco_min"))
    prec = parse_brl(request.form.get("preco_rec"))
    fonte = (request.form.get("fonte") or "").strip()

    propostas = []
    nomes = request.form.getlist("proposta_nome")
    valores = request.form.getlist("proposta_valor")
    for nome, valor in zip(nomes, valores):
        v = parse_brl(valor)
        if v is not None and v > 0:
            propostas.append({"nome": nome.strip(), "valor": v})

    if not pmin or not prec:
        flash("Informe o preço da configuração mínima e o da recomendada.", "erro")
    elif prec < pmin:
        flash("O preço da configuração recomendada não pode ser menor que o da mínima.", "erro")
    else:
        est["precos"] = {"min": pmin, "rec": prec, "fonte": fonte, "propostas": propostas}
    return _voltar("preco")


# --------------------------------------------------------------------------- cotação
@bp.route("/resultado/estados", methods=["POST"])
def estados():
    est = estado.obter()
    acao = request.form.get("acao")
    uf = request.form.get("uf", "")

    if acao == "adicionar" and uf in ESTADOS_POR_UF and uf not in est["estados"]:
        est["estados"].append(uf)
    elif acao == "remover" and uf in est["estados"] and len(est["estados"]) > 1:
        est["estados"].remove(uf)
    elif acao == "remover":
        flash("Mantenha ao menos um estado na busca.", "aviso")
    elif acao == "todos":
        est["estados"] = [e[0] for e in ESTADOS]
    return _voltar("regioes")


@bp.route("/resultado/contatos", methods=["POST"])
def contatos():
    est = estado.obter()
    acao = request.form.get("acao")

    if acao == "adicionar":
        empresa = (request.form.get("empresa") or "").strip()
        if not empresa:
            flash("Informe o nome da empresa contatada.", "erro")
        else:
            resposta = request.form.get("resposta")
            est["contatos"].append({
                "empresa": empresa,
                "data": request.form.get("data") or hoje_iso(),
                "resposta": resposta if resposta in RESPOSTAS else RESPOSTAS[0],
            })
    else:
        try:
            i = int(request.form.get("indice", ""))
            if acao == "remover":
                est["contatos"].pop(i)
            elif acao == "atualizar":
                resposta = request.form.get("resposta")
                if resposta in RESPOSTAS:
                    est["contatos"][i]["resposta"] = resposta
        except (ValueError, IndexError):
            pass
    return _voltar("contatos")


@bp.route("/resultado/conferido", methods=["POST"])
def conferido():
    est = estado.obter()
    fid = request.form.get("id", "")
    if fid:
        est["conferidos"][fid] = hoje_iso()
    return _voltar("pontos")
