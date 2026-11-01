# PC Público Inteligente

Pré-validação de compras de computadores para órgãos públicos, em Python (Flask).
O órgão marca a finalidade do computador e recebe o mínimo, o alvo e o recomendado de hardware,
com um caminho para **licitação pública** e outro para **cotação com fornecedores**.

> Todos os requisitos por software e todos os nomes de empresas são **fictícios**, como pedem os documentos.

## Como rodar no VS Code

1. Abra a pasta `pc_publico_inteligente` no VS Code (Arquivo > Abrir Pasta).
2. Abra o terminal (Ctrl + ') e crie o ambiente virtual:
   ```
   python -m venv .venv
   ```
3. Ative o ambiente:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
4. Instale o Flask:
   ```
   pip install -r requirements.txt
   ```
5. Rode:
   ```
   python app.py
   ```
6. Abra no navegador: http://127.0.0.1:5000

## Onde mexer (cada aba tem seus arquivos)

| Aba | Rota (lógica) | Tela (HTML) | JavaScript |
|---|---|---|---|
| Início | `rotas/inicio.py` | `templates/inicio.html` | |
| 01 Tipo e finalidade | `rotas/etapa1.py` | `templates/etapa1.html` | `static/js/etapa1.js` |
| 02 Detalhes de uso | `rotas/etapa2.py` | `templates/etapa2.html` | |
| 03 Resultado (licitação) | `rotas/resultado.py` | `templates/resultado_licitacao.html` | `static/js/resultado.js` |
| 03 Resultado (cotação) | `rotas/resultado.py` | `templates/resultado_cotacao.html` | |
| Conferir especificação | `rotas/conferir.py` | `templates/conferir.html` | |
| Relatório | `rotas/relatorio.py` | `templates/relatorio.html` | |

### Dados (trocar os números fictícios por oficiais)
- `dados/softwares.py`: requisitos mínimo e recomendado de cada software e o campo `fonte`.
- `dados/finalidades.py`: lista de finalidades e quais softwares aparecem/vêm marcados.
- `dados/fornecedores.py`: lista curada de empresas reais por estado (`CURADOS`). Enquanto estiver vazia, o programa gera nomes genéricos.
- `dados/estados.py`: estados e cidades usados nos exemplos.

### Regras e textos
- `servicos/calculo.py`: como multitarefa, vida útil, dados locais e usuários mudam o cálculo; como o alvo é calculado.
- `servicos/textos.py`: texto da especificação, da justificativa do ETP e do pedido de orçamento.
- `servicos/precos.py`: régua de preço e posição de cada proposta.
- `servicos/alertas.py`: listas de fabricantes, linhas de produto e gerações; leitura do texto do edital.
- `servicos/fornecedores.py`: pontos de busca por estado e valores da consulta (R$ 15 / 20 / 30 / 50).

### Aparência
- `static/css/estilo.css`: cores nas variáveis do topo do arquivo (`:root`).
- `templates/base.html`: cabeçalho, menu de abas e rodapé comuns a todas as telas.
- `config.py`: nome do site, porta e textos de aviso.
- `abas.py`: ordem e nome das abas do menu.

## Como o programa funciona

1. **Tipo de contratação** e **finalidade** (etapa 01) definem os softwares marcados.
2. **Detalhes de uso** (etapa 02) registram multitarefa, vida útil, dados locais e usuários, e permitem editar o requisito de cada software com a fonte.
3. O cálculo pega o maior requisito entre os softwares, aplica as condições e gera **mínimo, alvo e recomendado**.
4. Saída A, **licitação**: tabela dos três valores, régua de preço (o usuário informa o preço da mínima e da recomendada; o valor médio é a média dos dois), especificação por desempenho e justificativa para o ETP, com alerta de marca/modelo/geração.
5. Saída B, **cotação**: escolha de estados, texto padrão do pedido de orçamento, registro de contatos e pontos de busca por estado (ordem alfabética, sem preço, com data da última conferência).
6. **Conferir especificação**: cola um texto de edital, compara com o cálculo em gráfico de barras e alerta sobre capacidade acima da referência e sobre marca, modelo ou geração.

## Limites da ferramenta

Apoio à análise técnica. Não recomenda marca, não conclui sobre irregularidade e não substitui o parecer dos profissionais responsáveis e do jurídico.

## Observação técnica

As respostas ficam na memória do servidor (`estado.py`) e somem ao reiniciar o programa. Para guardar consultas de forma permanente, troque `estado.py` por um banco de dados (SQLite, por exemplo) mantendo as funções `obter()` e `reiniciar()`.
