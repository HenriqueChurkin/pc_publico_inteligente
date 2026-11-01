"""Configurações gerais do programa.

Se quiser mudar a porta, o endereço ou a chave de segurança, é aqui.
"""
import os

SECRET_KEY = os.environ.get("PCPI_SECRET", "troque-esta-chave-antes-de-publicar")
DEBUG = True

HOST = "127.0.0.1"
PORT = 5000

# Textos que aparecem em várias telas (mude aqui e muda em todas)
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
