"""Geração dos textos: especificação por desempenho, justificativa do ETP e pedido de orçamento."""
from dados.componentes import GPU_CURTO, GPU_ROTULOS
from servicos.formatacao import brl, fmt_ram, fmt_ssd


def _valores(calc, nivel):
    chave = "minimo" if nivel == "minimo" else "alvo"
    return calc[chave]


# ---------------------------------------------------------------------------
# Licitação pública: especificação por desempenho (sem marca, modelo ou geração)
# ---------------------------------------------------------------------------
def especificacao(calc, nivel="alvo"):
    v = _valores(calc, nivel)
    linhas = [
        f"Memória RAM: no mínimo {fmt_ram(v['ram'])}.",
        f"Armazenamento: unidade de estado sólido (SSD) com no mínimo {fmt_ssd(v['ssd'])}.",
        f"Processador: desempenho igual ou superior a [pontuação em benchmark público "
        f"correspondente à classe {int(v['cpu'])}, a definir].",
    ]
    if int(v["gpu"]) == 0:
        linhas.append("Vídeo: integrado, sem exigência de placa dedicada.")
    else:
        linhas.append(
            "Vídeo: dedicado, com desempenho gráfico igual ou superior a [pontuação em "
            f"benchmark público correspondente ao nível {GPU_CURTO[int(v['gpu'])]}, a definir]."
        )
    linhas.append("")
    linhas.append('Não indicar marca, modelo ou geração. Aceitar produto "equivalente ou superior".')
    return "\n".join(linhas)


def justificativa(est_ctx):
    """Lista de frases para o Estudo Técnico Preliminar.

    est_ctx: dict com finalidade_nome, softwares, calc, nivel, precos (ou None)
    """
    calc = est_ctx["calc"]
    cond = calc["cond"]
    sws = est_ctx["softwares"]
    nivel = est_ctx["nivel"]

    itens = [
        f"Finalidade: {est_ctx['finalidade_nome'].lower()}, com os softwares "
        + ", ".join(s["nome"] for s in sws) + ".",
        "Requisitos de cada software, com fonte registrada: "
        + "; ".join(f"{s['nome']} (fonte: {s['fonte']})" for s in sws) + ".",
        f"Mínimo e recomendado calculados para vida útil de {cond['vida_util']} anos, "
        f"multitarefa {cond['multitarefa']}, {cond['usuarios']} usuário(s) simultâneo(s)"
        + (f" e {cond['dados_locais_gb']} GB de dados guardados localmente." if cond["dados_locais_gb"] else
           " e sem dados guardados localmente."),
    ]
    if nivel == "alvo":
        itens.append(
            "A especificação adota o alvo, calculado como a média entre o mínimo e o recomendado. "
            "No critério de menor preço, a proposta vencedora tende ao piso da especificação; "
            "exigir acima do mínimo é uma premissa deste projeto e se justifica para que a proposta "
            "de menor preço cubra a necessidade real de uso."
        )
    else:
        itens.append(
            "A especificação adota o mínimo calculado. Atenção: no critério de menor preço, a proposta "
            "vencedora tende ao piso da especificação, e o mínimo pode não cobrir toda a necessidade de uso."
        )
    p = est_ctx.get("precos")
    if p and p.get("regua"):
        r = p["regua"]
        fonte = p.get("fonte") or "pesquisa de preços do órgão"
        itens.append(
            f"Referência de preço pela média das duas configurações: {brl(r['media'])} "
            f"(mínima {brl(r['minimo'])}, recomendada {brl(r['recomendado'])}), fonte: {fonte}. "
            "Serve para avaliar se as propostas cobrem a necessidade real; não substitui a pesquisa "
            "de preços que define o valor estimado da contratação."
        )
    return itens


# ---------------------------------------------------------------------------
# Cotação com fornecedores: texto padrão do pedido de orçamento
# ---------------------------------------------------------------------------
def _faixa(minimo, recomendado, fmt):
    if minimo == recomendado:
        return fmt(minimo)
    return f"mínimo de {fmt(minimo)}, recomendado {fmt(recomendado)}"


def _video(mn, rc):
    gmn, grc = int(mn["gpu"]), int(rc["gpu"])
    if gmn == 0 and grc == 0:
        return "Vídeo integrado"
    if gmn == 0:
        return f"Vídeo integrado (mínimo) ou dedicado {GPU_CURTO[grc]} (recomendado)"
    if gmn == grc:
        return f"Vídeo dedicado, {GPU_CURTO[gmn]}"
    return f"Vídeo dedicado, {GPU_CURTO[gmn]} a {GPU_CURTO[grc]}"


def pedido_orcamento(calc, finalidade_nome):
    mn, rc = calc["minimo"], calc["recomendado"]
    cpu = (f"classe de desempenho {int(mn['cpu'])}" if mn["cpu"] == rc["cpu"]
           else f"classe de desempenho {int(mn['cpu'])} a {int(rc['cpu'])}")
    return "\n".join([
        f"Solicitamos orçamento para computadores com a seguinte especificação, "
        f"para uso em {finalidade_nome.lower()}:",
        f"- Memória RAM: {_faixa(mn['ram'], rc['ram'], fmt_ram)}",
        f"- Armazenamento SSD: {_faixa(mn['ssd'], rc['ssd'], fmt_ssd)}",
        f"- Processador: {cpu}",
        f"- {_video(mn, rc)}",
        "",
        "Indicar garantia, prazo de entrega e se atende pessoa jurídica. "
        "Aceitaremos produtos equivalentes ou superiores.",
    ])
