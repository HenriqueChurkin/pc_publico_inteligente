"""Escalas dos componentes e estimativas de preço de referência.

Estimativas de preço baseadas em:
  - Painel de Preços do Governo Federal (paineldeprecos.economia.gov.br)
  - Banco de Preços em Saúde (bps.saude.gov.br) — referência subsidiária para equipamentos
  Observação: os preços abaixo são médias aproximadas para uso como referência inicial
  na elaboração do Estudo Técnico Preliminar. O valor estimado da contratação deve ser
  obtido mediante pesquisa de preços formal, conforme o art. 23 da Lei 14.133/2021 e
  a Instrução Normativa SEGES/ME nº 65/2021.
"""

RAM_PASSOS = [4, 8, 16, 32, 64, 128]
SSD_PASSOS = [128, 256, 512, 1024, 2048, 4096]
CPU_MIN, CPU_MAX = 1, 5

GPU_ROTULOS = {
    0: "Integrada",
    1: "Dedicada de entrada",
    2: "Dedicada intermediária",
    3: "Dedicada avançada",
}
GPU_CURTO = {1: "de entrada", 2: "intermediário", 3: "avançado"}

COMPONENTES = [
    ("ram", "Memória RAM"),
    ("ssd", "Armazenamento (SSD)"),
    ("cpu", "Processador"),
    ("gpu", "Placa de vídeo"),
]

# Preços médios de referência (R$) — baseados no Painel de Preços (paineldeprecos.economia.gov.br).
# Representam o custo unitário do componente isolado, não o custo do equipamento completo.
# Variação regional e de mercado pode chegar a ±25%. Consulte sempre o Painel de Preços
# para o valor atualizado antes de elaborar o TR ou o ETP.
PRECO_RAM = {4: 120, 8: 220, 16: 400, 32: 750, 64: 1500, 128: 2800}
PRECO_SSD = {128: 100, 256: 160, 512: 260, 1024: 420, 2048: 750, 4096: 1400}
PRECO_CPU = {1: 350, 2: 650, 3: 1000, 4: 1700, 5: 3000}
PRECO_GPU = {0: 0, 1: 550, 2: 1300, 3: 2800}

# Base do equipamento (gabinete, placa-mãe, fonte, etc.) — estimativa de referência
PRECO_BASE = 750


def preco_config(cpu, ram, ssd, gpu):
    """Calcula preço estimado somando componentes + base."""
    total = (PRECO_BASE
             + PRECO_CPU.get(int(cpu), 650)
             + PRECO_RAM.get(int(ram), 220)
             + PRECO_SSD.get(int(ssd), 160)
             + PRECO_GPU.get(int(gpu), 0))
    return total


def faixa_preco(calc):
    """Retorna preços mínimo, recomendado e variação estimada.

    A variação de ±25% reflete diferenças de marca, região e momento da compra,
    conforme observado no histórico do Painel de Preços do Governo Federal.
    """
    mn = calc["minimo"]
    rc = calc["recomendado"]
    p_min = preco_config(mn["cpu"], mn["ram"], mn["ssd"], mn["gpu"])
    p_rec = preco_config(rc["cpu"], rc["ram"], rc["ssd"], rc["gpu"])
    variacao = 0.25
    return p_min, p_rec, variacao


CATEGORIA_LABEL = {
    "basico":        "Básico",
    "intermediario": "Intermediário",
    "avancado":      "Avançado",
    "alto":          "Alto desempenho",
    "workstation":   "Workstation",
}

# Fonte de referência para pesquisa de preços
FONTE_PRECOS = "https://paineldeprecos.economia.gov.br"
NOTA_PRECOS = (
    "Estimativas de referência. Realize pesquisa de preços no Painel de Preços "
    "(paineldeprecos.economia.gov.br) para o valor estimado da contratação, "
    "conforme o art. 23 da Lei 14.133/2021 e a IN SEGES/ME nº 65/2021."
)
