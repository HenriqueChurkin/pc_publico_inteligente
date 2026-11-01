"""Finalidades — 9 programas por categoria."""

FINALIDADES = [
    {
        "id": "administrativo",
        "nome": "Trabalho administrativo e de escritório",
        "descricao": "Digitar documentos, responder e-mails, usar sistemas do governo",
        "icone": "📋",
        "opcoes": ["escritorio", "navegador", "email", "sistema_corporativo", "pdf", "videoconferencia", "chat_suporte", "formularios_gov", "assinatura_digital"],
        "padrao": ["escritorio", "navegador", "email", "sistema_corporativo"],
    },
    {
        "id": "atendimento",
        "nome": "Atendimento ao público",
        "descricao": "Receber pessoas, usar sistema de atendimento, fazer videochamadas",
        "icone": "🧑‍💼",
        "opcoes": ["videoconferencia", "sistema_atendimento", "chat_suporte", "navegador", "escritorio", "email", "pdf", "formularios_gov", "sistema_corporativo"],
        "padrao": ["videoconferencia", "sistema_atendimento", "navegador"],
    },
    {
        "id": "projeto",
        "nome": "Projetos e desenhos técnicos",
        "descricao": "Criar plantas, projetos de engenharia, arquitetura ou infraestrutura",
        "icone": "📐",
        "opcoes": ["autocad", "revit", "sketchup", "visualizador3d", "escritorio", "navegador", "pdf", "calculo_estrutural", "renderizacao"],
        "padrao": ["autocad", "escritorio", "navegador"],
    },
    {
        "id": "edicao",
        "nome": "Criação de conteúdo visual",
        "descricao": "Editar fotos, vídeos, criar materiais gráficos para comunicação",
        "icone": "🎨",
        "opcoes": ["editor_imagem", "editor_video", "ilustracao", "audio", "escritorio", "navegador", "pdf", "animacao", "captura_tela"],
        "padrao": ["editor_imagem", "escritorio", "navegador"],
    },
    {
        "id": "geoprocessamento",
        "nome": "Mapas e geoprocessamento",
        "descricao": "Trabalhar com mapas, imagens de satélite, drones ou SIG",
        "icone": "🗺️",
        "opcoes": ["sig", "sensoriamento", "drone", "visualizador3d", "escritorio", "navegador", "banco_dados", "estatistica", "pdf"],
        "padrao": ["sig", "escritorio", "navegador"],
    },
    {
        "id": "laboratorio",
        "nome": "Sala de aula ou laboratório",
        "descricao": "Ensino, treinamento, atividades educativas com alunos ou servidores",
        "icone": "🏫",
        "opcoes": ["editores_ensino", "ambiente_ensino", "programacao", "navegador", "escritorio", "videoconferencia", "editor_imagem", "pdf", "audio"],
        "padrao": ["editores_ensino", "ambiente_ensino", "navegador"],
    },
    {
        "id": "dados",
        "nome": "Análise de dados e relatórios",
        "descricao": "Trabalhar com grandes planilhas, gerar relatórios, usar BI ou estatística",
        "icone": "📊",
        "opcoes": ["planilhas_avancadas", "bi", "estatistica", "banco_dados", "escritorio", "navegador", "pdf", "visualizacao_dados", "automacao"],
        "padrao": ["planilhas_avancadas", "bi", "escritorio"],
    },
    {
        "id": "ti",
        "nome": "Tecnologia da Informação (TI)",
        "descricao": "Desenvolvimento de sistemas, banco de dados, infraestrutura de TI",
        "icone": "💻",
        "opcoes": ["programacao", "banco_dados", "bi", "estatistica", "navegador", "escritorio", "ambiente_ensino", "automacao", "virtualizacao"],
        "padrao": ["programacao", "banco_dados", "navegador"],
    },
    {
        "id": "outra",
        "nome": "Outra necessidade",
        "descricao": "Digite os programas que serão usados",
        "icone": "⚙️",
        "opcoes": [],
        "padrao": [],
    },
]

FINALIDADES_POR_ID = {f["id"]: f for f in FINALIDADES}
