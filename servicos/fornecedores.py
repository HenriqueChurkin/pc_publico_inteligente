"""Pontos de busca de fornecedores por estado (Fluxo B: cotação).

Regras da lista (do documento de pré-validação):
  - ordem alfabética dentro de cada categoria, sem ordem de preferência
  - sem preço, sem avaliação, sem destaque para nenhuma empresa
  - data da última conferência em cada item
  - campo "atende pessoa jurídica" sempre a confirmar
"""
from dados.estados import ESTADOS, ESTADOS_POR_UF
from dados.fornecedores import CATEGORIAS, CURADOS

# Valores de consulta do MVP (modelo de negócio para validação)
PRECOS_CONSULTA = {1: 15, 2: 20, 3: 30}
PRECO_NACIONAL = 50


def preco_consulta(qtd_estados):
    """Devolve o valor da consulta ou None quando a faixa ainda não foi definida."""
    if qtd_estados >= len(ESTADOS):
        return PRECO_NACIONAL
    return PRECOS_CONSULTA.get(qtd_estados)


def _letra(i, mult, desloc):
    return chr(65 + (i * mult + desloc) % 26)


def _itens_ficticios(uf):
    indice = [e[0] for e in ESTADOS].index(uf)
    _, _, capital, interior = ESTADOS_POR_UF[uf]
    return {
        "distribuidores": [{"nome": f"Distribuidora Exemplo {_letra(indice, 3, 0)}", "local": capital}],
        "revendas": [{"nome": f"Revenda Exemplo {_letra(indice, 5, 1)}", "local": interior}],
        "varejistas": [{"nome": f"Loja Exemplo {_letra(indice, 7, 2)}", "local": f"Online e lojas em {uf}"}],
        "online": [{"nome": f"Loja Online Exemplo {_letra(indice, 11, 3)}",
                    "local": f"Venda online com envio para {uf}"}],
    }


def pontos_de_busca(uf, conferidos):
    """Lista de categorias, cada uma com itens em ordem alfabética."""
    curado = uf in CURADOS
    base = CURADOS[uf] if curado else _itens_ficticios(uf)

    categorias = []
    for cat_id, cat_nome in CATEGORIAS:
        itens = []
        for n, item in enumerate(base.get(cat_id, []), start=1):
            fid = f"{uf}-{cat_id}-{n}"
            itens.append({
                "id": fid,
                "nome": item["nome"],
                "local": item.get("local", ""),
                "atende_pj": item.get("atende_pj", "a confirmar"),
                "ultima_conferencia": conferidos.get(fid) or item.get("ultima_conferencia"),
                "ficticio": not curado,
            })
        itens.sort(key=lambda x: x["nome"].lower())
        if itens:
            categorias.append({"id": cat_id, "nome": cat_nome, "itens": itens})
    return categorias
