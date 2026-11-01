"""Requisitos por software (DADOS FICTÍCIOS).

Quando houver documentação oficial dos fabricantes, troque os números abaixo
e preencha o campo "fonte" com o link ou o nome do documento.

Cada software tem um mínimo ("min") e um recomendado ("rec"):
  ram = GB de memória | ssd = GB de armazenamento
  cpu = classe do processador (1 a 5) | gpu = 0 integrada, 1 entrada, 2 intermediária, 3 avançada
"""


def _req(ram, ssd, cpu, gpu):
    return {"ram": ram, "ssd": ssd, "cpu": cpu, "gpu": gpu}


FONTE_FICTICIA = "fictícia"

SOFTWARES = {
    "escritorio": {
        "nome": "Pacote de escritório",
        "min": _req(4, 128, 2, 0), "rec": _req(8, 256, 3, 0),
    },
    "navegador": {
        "nome": "Navegador web",
        "min": _req(4, 128, 2, 0), "rec": _req(8, 256, 3, 0),
    },
    "sistema_corporativo": {
        "nome": "Sistema corporativo",
        "min": _req(4, 128, 2, 0), "rec": _req(8, 256, 2, 0),
    },
    "sistema_atendimento": {
        "nome": "Sistema de atendimento",
        "min": _req(4, 128, 2, 0), "rec": _req(8, 256, 3, 0),
    },
    "videoconferencia": {
        "nome": "Videoconferência",
        "min": _req(8, 256, 3, 0), "rec": _req(16, 256, 4, 0),
    },
    "autocad": {
        "nome": "AutoCAD ou equivalente",
        "min": _req(8, 256, 3, 1), "rec": _req(16, 512, 4, 2),
    },
    "visualizador3d": {
        "nome": "Visualizador de modelos 3D",
        "min": _req(8, 256, 3, 1), "rec": _req(16, 512, 4, 2),
    },
    "editor_imagem": {
        "nome": "Editor de imagem",
        "min": _req(16, 512, 3, 1), "rec": _req(32, 1024, 4, 2),
    },
    "editor_video": {
        "nome": "Editor de vídeo",
        "min": _req(16, 512, 4, 1), "rec": _req(32, 1024, 5, 2),
    },
    "sig": {
        "nome": "Software de geoprocessamento (SIG)",
        "min": _req(16, 512, 3, 1), "rec": _req(32, 1024, 4, 2),
    },
    "editores_ensino": {
        "nome": "Editores (texto, planilha, apresentação)",
        "min": _req(4, 128, 2, 0), "rec": _req(8, 256, 3, 0),
    },
    "ambiente_ensino": {
        "nome": "Ambientes de ensino",
        "min": _req(8, 256, 3, 0), "rec": _req(16, 256, 3, 0),
    },
}

for _id, _sw in SOFTWARES.items():
    _sw["id"] = _id
    _sw["fonte"] = FONTE_FICTICIA

# Usado quando a finalidade é "Outra (inserir requisitos manualmente)"
MANUAL = {
    "id": "manual",
    "nome": "Requisitos informados manualmente",
    "fonte": "informado pelo órgão",
    "min": _req(8, 256, 3, 0),
    "rec": _req(16, 512, 4, 0),
}
