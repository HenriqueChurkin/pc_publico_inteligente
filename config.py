"""Configurações gerais do programa."""
import os

SECRET_KEY = os.environ.get("PCPI_SECRET", "troque-esta-chave-antes-de-publicar")
DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))

NOME_SITE = "PC Público Inteligente"
SUBTITULO_SITE = "Pré-validação de compras de computadores para órgãos públicos"
AVISO_DEMO = (
    "Dados de demonstração fictícios. Os requisitos por finalidade ainda não vêm "
    "de documentação oficial e os nomes de empresas são genéricos."
)
LIMITES_FERRAMENTA = (
    "Apoio à análise técnica. Não recomenda marca, não conclui sobre irregularidade "
    "e não substitui o parecer dos profissionais responsáveis e do jurídico."
)
