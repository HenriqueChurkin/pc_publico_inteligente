"""Lista de finalidades do computador.

"opcoes"  = softwares que aparecem na lista da etapa 1
"padrao"  = softwares que já vêm marcados
Para criar uma finalidade nova, copie um bloco e use ids que existam em softwares.py.
"""

FINALIDADES = [
    {
        "id": "administrativo",
        "nome": "Administrativo e escritório",
        "efeito": "Processador de entrada, memória moderada, vídeo integrado.",
        "opcoes": ["escritorio", "navegador", "sistema_corporativo", "videoconferencia"],
        "padrao": ["escritorio", "navegador", "sistema_corporativo"],
    },
    {
        "id": "videoconferencia",
        "nome": "Atendimento com videoconferência",
        "efeito": "Processador intermediário, memória moderada, vídeo integrado.",
        "opcoes": ["videoconferencia", "navegador", "sistema_atendimento", "escritorio"],
        "padrao": ["videoconferencia", "navegador", "sistema_atendimento"],
    },
    {
        "id": "projeto",
        "nome": "Projeto e desenho técnico",
        "efeito": "Processador e memória mais altos, vídeo dedicado.",
        "opcoes": ["autocad", "navegador", "escritorio", "visualizador3d", "videoconferencia"],
        "padrao": ["autocad", "navegador", "escritorio"],
    },
    {
        "id": "edicao",
        "nome": "Edição de imagem e vídeo",
        "efeito": "Memória e armazenamento altos, vídeo dedicado.",
        "opcoes": ["editor_imagem", "editor_video", "navegador", "escritorio"],
        "padrao": ["editor_imagem", "editor_video", "navegador"],
    },
    {
        "id": "geoprocessamento",
        "nome": "Geoprocessamento",
        "efeito": "Memória alta, vídeo dedicado, armazenamento amplo.",
        "opcoes": ["sig", "navegador", "escritorio", "visualizador3d"],
        "padrao": ["sig", "navegador", "escritorio"],
    },
    {
        "id": "laboratorio",
        "nome": "Laboratório ou sala de aula",
        "efeito": "Perfil moderado, foco em robustez e quantidade.",
        "opcoes": ["navegador", "editores_ensino", "escritorio", "ambiente_ensino"],
        "padrao": ["navegador", "editores_ensino", "ambiente_ensino"],
    },
    {
        "id": "outra",
        "nome": "Outra (inserir requisitos manualmente)",
        "efeito": "Você informa os requisitos na etapa 2.",
        "opcoes": [],
        "padrao": [],
    },
]

FINALIDADES_POR_ID = {f["id"]: f for f in FINALIDADES}
