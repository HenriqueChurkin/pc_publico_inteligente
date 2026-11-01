"""Funções de formatação e leitura de valores (números, moeda, datas)."""
import re
from datetime import date

from dados.componentes import GPU_ROTULOS


def brl(valor):
    """5500 -> 'R$ 5.500,00'"""
    if valor is None or valor == "":
        return "—"
    texto = f"{float(valor):,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


def brl_curto(valor):
    """5500 -> 'R$ 5.500' (sem centavos, para a régua)"""
    return brl(valor).replace(",00", "")


def data_br(iso):
    """'2026-10-31' -> '31/10/2026'"""
    if not iso:
        return "—"
    try:
        return date.fromisoformat(iso).strftime("%d/%m/%Y")
    except ValueError:
        return iso


def hoje_iso():
    return date.today().isoformat()


def parse_brl(texto):
    """Lê '4.200,00', '4200', 'R$ 4200,5' e devolve float. Devolve None se não der."""
    if texto is None:
        return None
    t = str(texto).replace("R$", "").replace(" ", "").strip()
    if not t:
        return None
    if "," in t:
        t = t.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", t):
        t = t.replace(".", "")
    try:
        valor = float(t)
    except ValueError:
        return None
    return valor if valor >= 0 else None


def parse_int(texto, padrao, minimo=None, maximo=None):
    try:
        valor = int(str(texto).strip())
    except (ValueError, TypeError):
        return padrao
    if minimo is not None:
        valor = max(minimo, valor)
    if maximo is not None:
        valor = min(maximo, valor)
    return valor


# --- texto de cada componente ------------------------------------------------

def fmt_ram(n):
    return f"{n:g} GB"


def fmt_ssd(n):
    if n >= 1024 and n % 1024 == 0:
        return f"{int(n // 1024)} TB"
    return f"{n:g} GB"


def fmt_cpu(n):
    return f"Classe {int(n)}"


def fmt_gpu(n):
    return GPU_ROTULOS.get(int(n), "—")


def formatar_componente(comp_id, valor):
    return {"ram": fmt_ram, "ssd": fmt_ssd, "cpu": fmt_cpu, "gpu": fmt_gpu}[comp_id](valor)
