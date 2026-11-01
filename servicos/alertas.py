"""Conferência de uma especificação já redigida.

- detectar_termos(): acha fabricante, linha de produto e geração no texto
- extrair_requisitos(): lê RAM, SSD, classe do processador e tipo de vídeo do texto
- comparar(): compara o que foi lido com o cálculo (mínimo / recomendado)

As listas abaixo são simples de editar: é só incluir mais palavras.
"""
import re

FABRICANTES = [
    "intel", "amd", "nvidia", "dell", "hp", "lenovo", "acer", "asus", "apple", "samsung",
    "positivo", "multilaser", "microsoft", "qualcomm", "msi", "gigabyte", "kingston",
    "western digital", "seagate", "crucial", "corsair", "logitech", "huawei", "xiaomi",
    "itautec", "vaio", "toshiba", "lg", "sony", "cce", "hyperx", "sandisk", "adata",
]

LINHAS = [
    r"core\s*i[3579]", r"core\s*ultra", r"i[3579]-?\d{3,5}[a-z]{0,2}", r"ryzen(?:\s*[3579])?",
    r"threadripper", r"xeon", r"celeron", r"pentium", r"athlon", r"geforce", r"radeon",
    r"quadro", r"rtx", r"gtx", r"iris\s*xe", r"uhd\s*graphics", r"thinkcentre", r"thinkpad",
    r"optiplex", r"inspiron", r"vostro", r"latitude", r"precision", r"elitedesk", r"prodesk",
    r"probook", r"elitebook", r"ideapad", r"ideacentre", r"vivobook", r"aspire", r"macbook",
    r"imac", r"mac\s*mini", r"galaxy\s*book", r"surface", r"arc\s*a\d{3}",
]

GERACAO = [
    r"\d{1,2}\s*[ªa°º]?\s*(?:geração|geracao|gen)\b",
    r"\d{1,2}(?:st|nd|rd|th)\s*gen(?:eration)?\b",
    r"gera[çc][ãa]o\s*\d{1,2}\b",
]


def detectar_termos(texto):
    """Devolve lista de {"termo", "tipo"} sem repetição."""
    achados, vistos = [], set()

    def add(termo, tipo):
        chave = (termo.lower(), tipo)
        if chave not in vistos:
            vistos.add(chave)
            achados.append({"termo": termo, "tipo": tipo})

    for f in FABRICANTES:
        for m in re.finditer(rf"(?<![\wÀ-ÿ]){re.escape(f)}(?![\wÀ-ÿ])", texto, re.IGNORECASE):
            add(m.group(0), "fabricante")
    for padrao in LINHAS:
        for m in re.finditer(rf"(?<![\wÀ-ÿ]){padrao}(?![\wÀ-ÿ])", texto, re.IGNORECASE):
            add(m.group(0), "linha de produto")
    for padrao in GERACAO:
        for m in re.finditer(padrao, texto, re.IGNORECASE):
            add(m.group(0), "geração")
    return achados


# ---------------------------------------------------------------------------
_FIM_FRASE = r"[.;\n](?:\s|$)"
_QUANTIDADE = r"(\d+(?:[.,]\d+)?)\s*(tb|gb|gigabytes?|terabytes?)"

_PALAVRAS = {
    "ram": ["ram", "memória", "memoria", "ddr"],
    "ssd": ["ssd", "armazenamento", "disco", "hd", "nvme", "estado sólido", "estado solido"],
}


def _capacidades(t):
    """Liga cada quantidade (ex.: 16 GB) à palavra-chave mais próxima (RAM ou SSD).

    Funciona nas duas ordens: "RAM: 16 GB" e "16 GB de RAM". Cada palavra e cada
    quantidade só é usada uma vez, então "16 GB de RAM e 1 TB de SSD" sai certo.
    """
    res = {"ram": None, "ssd": None}
    for frase in re.split(_FIM_FRASE, t):
        quants = []
        for m in re.finditer(_QUANTIDADE, frase):
            valor = float(m.group(1).replace(",", "."))
            if m.group(2).startswith("t"):
                valor *= 1024
            quants.append((m.start(), m.end(), valor))

        palavras = []
        for tipo, lista in _PALAVRAS.items():
            for p in lista:
                for m in re.finditer(rf"(?<![a-zà-ÿ]){re.escape(p)}(?![a-zà-ÿ])", frase):
                    palavras.append((m.start(), m.end(), tipo))

        pares = []
        for qi, (qs, qe, _) in enumerate(quants):
            for ki, (ks, ke, _) in enumerate(palavras):
                if ke <= qs:                 # palavra antes do número: "RAM de 16 GB"
                    intervalo = frase[ke:qs]
                    if re.search(r"(\se\s|\sou\s|[,;/])", intervalo):
                        continue             # há outro item no meio ("... e SSD de 512 GB")
                    d = qs - ke
                elif ks >= qe:               # palavra depois do número: "16 GB de RAM"
                    intervalo = frase[qe:ks]
                    if not re.fullmatch(r"\s*(?:de|em|of)?\s*", intervalo):
                        continue             # só vale se a palavra vier logo em seguida
                    d = (ks - qe) + 0.5
                else:
                    continue
                if d <= 40:
                    pares.append((d, qi, ki))
        pares.sort()

        q_usadas, k_usadas, atribuido = set(), set(), {}
        for d, qi, ki in pares:
            if qi in q_usadas or ki in k_usadas:
                continue
            q_usadas.add(qi)
            k_usadas.add(ki)
            atribuido[qi] = palavras[ki][2]

        for qi in sorted(atribuido):
            tipo = atribuido[qi]
            if res[tipo] is None:
                res[tipo] = quants[qi][2]
    return res


def extrair_requisitos(texto):
    """Lê o texto e devolve {"ram": GB|None, "ssd": GB|None, "cpu": classe|None, "gpu": 0..3|None}."""
    t = texto.lower()
    res = {"ram": None, "ssd": None, "cpu": None, "gpu": None}
    res.update(_capacidades(t))

    m = re.search(r"classe\s*(?:de\s*desempenho\s*)?(\d)", t)
    if m:
        res["cpu"] = int(m.group(1))

    if re.search(r"\bdedicad", t):
        if re.search(r"avan[çc]ad|alto desempenho|alta performance", t):
            res["gpu"] = 3
        elif re.search(r"intermedi", t):
            res["gpu"] = 2
        else:
            res["gpu"] = 1
    elif re.search(r"\bintegrad", t):
        res["gpu"] = 0
    return res


def comparar(extraido, calc):
    """Para cada componente, diz se o valor do texto está abaixo, dentro ou acima da faixa."""
    linhas, alertas = [], []
    for comp in calc["componentes"]:
        cid = comp["id"]
        v = extraido.get(cid)
        if v is None:
            status = "nao_encontrado"
        elif v < comp["minimo"]:
            status = "abaixo_minimo"
            alertas.append(f"{comp['nome']}: o texto pede {_txt(cid, v)}, abaixo do mínimo calculado "
                           f"({comp['min_txt']}). A proposta de menor preço pode não atender à necessidade.")
        elif v > comp["recomendado"]:
            status = "acima_recomendado"
            alertas.append(f"{comp['nome']}: o texto pede {_txt(cid, v)}, acima da referência recomendada "
                           f"({comp['rec_txt']}). Exigir mais que a referência precisa de justificativa.")
        else:
            status = "dentro"
        linhas.append({"comp": comp, "valor": v, "valor_txt": _txt(cid, v) if v is not None else "—",
                       "status": status})
    return {"linhas": linhas, "alertas": alertas}


def _txt(cid, v):
    from servicos.formatacao import formatar_componente
    return formatar_componente(cid, v)


ROTULO_STATUS = {
    "nao_encontrado": "não encontrado no texto",
    "abaixo_minimo": "abaixo do mínimo",
    "dentro": "dentro da faixa",
    "acima_recomendado": "acima da recomendada",
}
