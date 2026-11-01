"""Régua de preço da licitação.

A ferramenta NÃO consulta preços: o usuário informa o preço da configuração mínima
e o da recomendada (vindos da pesquisa de preços do órgão). O valor médio é a média
dos dois, e cada proposta recebida é posicionada nessa régua.
"""

POSICOES = {
    "abaixo": ("Abaixo da mínima", "Se atende a toda a especificação mínima e se o preço é exequível."),
    "min_media": ("Entre a mínima e a média", "Se a configuração ofertada cobre a especificação mínima."),
    "media_rec": ("Entre a média e a recomendada",
                  "Se a diferença de preço corresponde a ganho real de configuração."),
    "acima": ("Acima da recomendada",
              "Se o valor excede a referência recomendada e se há justificativa para a diferença."),
}


def _posicao(valor, pmin, media, prec):
    if valor < pmin:
        return "abaixo"
    if valor < media:
        return "min_media"
    if valor <= prec:
        return "media_rec"
    return "acima"


def montar_regua(pmin, prec, propostas):
    """propostas: lista de {"nome": str, "valor": float}"""
    media = (pmin + prec) / 2
    valores = [pmin, prec] + [p["valor"] for p in propostas]
    lo = min(valores) * 0.9
    hi = max(valores) * 1.1
    if hi == lo:
        hi = lo + 1

    def pct(v):
        return round((v - lo) / (hi - lo) * 100, 2)

    segmentos = [
        {"cls": "abaixo", "left": 0, "width": pct(pmin), "rotulo": "abaixo da mínima"},
        {"cls": "min_media", "left": pct(pmin), "width": round(pct(media) - pct(pmin), 2),
         "rotulo": "entre mínima e média"},
        {"cls": "media_rec", "left": pct(media), "width": round(pct(prec) - pct(media), 2),
         "rotulo": "entre média e recomendada"},
        {"cls": "acima", "left": pct(prec), "width": round(100 - pct(prec), 2),
         "rotulo": "acima da recomendada"},
    ]

    itens = []
    for i, p in enumerate(propostas, start=1):
        pos = _posicao(p["valor"], pmin, media, prec)
        itens.append({
            "n": i,
            "nome": p["nome"] or f"Proposta {i}",
            "valor": p["valor"],
            "pct": pct(p["valor"]),
            "pos": pos,
            "pos_txt": POSICOES[pos][0],
            "verificar": POSICOES[pos][1],
        })

    return {
        "minimo": pmin, "recomendado": prec, "media": media,
        "pct_min": pct(pmin), "pct_media": pct(media), "pct_rec": pct(prec),
        "segmentos": segmentos, "propostas": itens,
    }
