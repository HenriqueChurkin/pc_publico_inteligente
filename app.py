"""Ponto de entrada do programa.

Para rodar:   python app.py
Depois abra:  http://127.0.0.1:5000
"""
from flask import Flask, request

import config
import estado
from abas import ABAS
from rotas import conferir, etapa1, etapa2, inicio, relatorio, resultado
from servicos.formatacao import brl, brl_curto, data_br, hoje_iso


def criar_app():
    app = Flask(__name__)
    app.config.from_object(config)

    for modulo in (inicio, etapa1, etapa2, resultado, conferir, relatorio):
        app.register_blueprint(modulo.bp)

    app.add_template_filter(brl, "brl")
    app.add_template_filter(brl_curto, "brl_curto")
    app.add_template_filter(data_br, "data_br")

    @app.context_processor
    def variaveis_globais():
        return {
            "abas": ABAS,
            "aba_atual": request.blueprint,
            "cfg": config,
            "hoje": hoje_iso(),
            "est": estado.obter(),
        }

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
