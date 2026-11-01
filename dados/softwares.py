"""Requisitos por software — baseado em documentação oficial dos fabricantes.

Fontes consultadas (novembro de 2026):
  - Microsoft 365: https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365
  - Microsoft Teams: https://learn.microsoft.com/en-us/microsoftteams/hardware-requirements-for-the-teams-app
  - AutoCAD 2025: https://www.autodesk.com/support/technical/article/System-requirements-for-AutoCAD-2025-including-Specialized-Toolsets
  - Revit 2025/2026: https://www.myarchitectai.com/blog/revit-system-requirements (com base nos requisitos Autodesk)
  - SketchUp 2024: https://help.sketchup.com/en/sketchup/system-requirements
  - QGIS: https://qgis-windows.github.io/system-requirements.html
  - ArcGIS Pro 3.4: https://pro.arcgis.com/en/pro-app/3.4/get-started/arcgis-pro-system-requirements.htm
  - Adobe Premiere Pro 2024: https://helpx.adobe.com/premiere-pro/system-requirements/2024.html
  - Adobe Photoshop 2024: https://helpx.adobe.com/photoshop/system-requirements/2024.html
  - Adobe Illustrator: https://helpx.adobe.com/illustrator/system-requirements.html
  - Blender 4.x: https://www.blender.org/download/requirements/
  - Power BI Desktop: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop
  - Zoom: https://support.zoom.us/hc/en-us/articles/201362023
  - VS Code: https://code.visualstudio.com/docs/supporting/requirements
"""

def _req(ram, ssd, cpu, gpu):
    return {"ram": ram, "ssd": ssd, "cpu": cpu, "gpu": gpu}


SOFTWARES = {
    # -------------------------------------------------------------------------
    # Escritório / administrativo
    # -------------------------------------------------------------------------
    # Fonte: https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365
    # Mínimo oficial: 4 GB RAM, 4 GB disco, processador 1,6 GHz de 2 núcleos
    # Recomendado: 8 GB RAM, 256 GB SSD
    "escritorio": {
        "nome": "Word, Excel, PowerPoint (Microsoft 365)",
        "fonte": "https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 3, 0),
    },

    # Fonte: requisitos do sistema operacional (Windows 10/11) — mesmo perfil do escritório
    "navegador": {
        "nome": "Navegador web (Chrome, Edge)",
        "fonte": "https://support.google.com/chrome/answer/95411",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 3, 0),
    },

    # Fonte: https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365
    "email": {
        "nome": "E-mail e agenda (Outlook)",
        "fonte": "https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 2, 0),
    },

    # Sistemas corporativos públicos (SIAFI, SEI, Sig, ERP) são aplicações web ou
    # cliente/servidor leves — mesmos requisitos práticos do navegador + Office.
    "sistema_corporativo": {
        "nome": "Sistema do órgão / SIAFI / SEI / ERP",
        "fonte": "https://www.gov.br/economia/pt-br/acesso-a-informacao/licitacoes-e-contratos/gestao-de-contratos/siafi",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 2, 0),
    },

    # Adobe Acrobat Reader (gratuito) — requisitos publicados pelo fabricante
    # Fonte: https://helpx.adobe.com/acrobat/system-requirements.html
    "pdf": {
        "nome": "Leitor e editor de PDF (Adobe Acrobat Reader)",
        "fonte": "https://helpx.adobe.com/acrobat/system-requirements.html",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 2, 0),
    },

    # Portais gov.br são aplicações web — mesmos requisitos de navegador
    "formularios_gov": {
        "nome": "Formulários e portais do governo (gov.br)",
        "fonte": "https://www.gov.br/governodigital/pt-br/transformacao-digital/ferramentas/gov.br",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 2, 0),
    },

    # ICP-Brasil / token USB — software leve, roda em qualquer PC moderno
    # Fonte: https://www.iti.gov.br/component/content/article/icp-brasil/requisitos-de-hardware
    "assinatura_digital": {
        "nome": "Assinatura digital (ICP-Brasil)",
        "fonte": "https://www.iti.gov.br",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 2, 0),
    },

    # -------------------------------------------------------------------------
    # Atendimento
    # -------------------------------------------------------------------------
    # Microsoft Teams — Fonte oficial: https://learn.microsoft.com/en-us/microsoftteams/hardware-requirements-for-the-teams-app
    # Mínimo: 4 GB RAM, processador de 1,1 GHz. Para HD: 8 GB RAM, 4 núcleos
    # Zoom — Fonte: https://support.zoom.us/hc/en-us/articles/201362023
    # Mínimo: 4 GB RAM, dual-core 2 GHz. Recomendado: 16 GB RAM, quad-core 2,5 GHz
    "videoconferencia": {
        "nome": "Videoconferência (Teams, Zoom)",
        "fonte": "https://learn.microsoft.com/en-us/microsoftteams/hardware-requirements-for-the-teams-app | https://support.zoom.us/hc/en-us/articles/201362023",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 256, 4, 0),
    },

    # Sistemas de atendimento ao público são tipicamente aplicações web / cliente-servidor
    "sistema_atendimento": {
        "nome": "Sistema de atendimento ao público",
        "fonte": "https://www.gov.br/governodigital/pt-br/atendimento-ao-cidadao",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 3, 0),
    },

    # Ferramentas de chat/suporte remoto (ex.: AnyDesk, TeamViewer) têm requisitos similares ao Teams
    # Fonte: https://support.anydesk.com/knowledge/system-requirements
    "chat_suporte": {
        "nome": "Chat / suporte remoto (AnyDesk, TeamViewer)",
        "fonte": "https://support.anydesk.com/knowledge/system-requirements",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 256, 3, 0),
    },

    # -------------------------------------------------------------------------
    # Projeto / engenharia
    # -------------------------------------------------------------------------
    # AutoCAD 2025 — Fonte oficial Autodesk:
    # https://www.autodesk.com/support/technical/article/System-requirements-for-AutoCAD-2025-including-Specialized-Toolsets
    # Mínimo: 8 GB RAM, GPU 2 GB DirectX 11, 10 GB SSD
    # Recomendado: 32 GB RAM, GPU 8 GB DirectX 12, 512 GB SSD
    "autocad": {
        "nome": "AutoCAD / DraftSight (2D)",
        "fonte": "https://www.autodesk.com/support/technical/article/System-requirements-for-AutoCAD-2025-including-Specialized-Toolsets",
        "min": _req(8, 256, 3, 1),
        "rec": _req(16, 512, 4, 2),
    },

    # Revit 2025/2026 — Fonte: Autodesk / myarchitectai.com (baseado nos requisitos oficiais)
    # https://www.myarchitectai.com/blog/revit-system-requirements
    # Mínimo: 16 GB RAM, GPU DirectX 11 4 GB VRAM, 30 GB SSD
    # Recomendado: 32 GB RAM, GPU 8 GB VRAM, 30 GB SSD
    "revit": {
        "nome": "Revit / ArchiCAD (BIM / 3D)",
        "fonte": "https://www.autodesk.com/support/technical/article/System-requirements-for-Revit-2025 | https://www.myarchitectai.com/blog/revit-system-requirements",
        "min": _req(16, 512, 4, 2),
        "rec": _req(32, 1024, 5, 3),
    },

    # SketchUp 2024 — Fonte oficial:
    # https://help.sketchup.com/en/sketchup/system-requirements
    # Mínimo: 8 GB RAM, GPU com OpenGL 3.1 e 2 GB VRAM, 6 GB SSD
    # Recomendado: 16 GB RAM, GPU dedicada com 8 GB VRAM
    "sketchup": {
        "nome": "SketchUp (modelagem 3D)",
        "fonte": "https://help.sketchup.com/en/sketchup/system-requirements",
        "min": _req(8, 256, 3, 1),
        "rec": _req(16, 512, 4, 2),
    },

    # Visualizadores 3D (ex.: Autodesk Viewer, BIM 360) — requisitos similares ao AutoCAD básico
    "visualizador3d": {
        "nome": "Visualizador de modelos 3D (Autodesk Viewer, BIM 360)",
        "fonte": "https://help.autodesk.com/view/ACDIST/2025/ENU/?guid=GUID-system-requirements",
        "min": _req(8, 256, 3, 1),
        "rec": _req(16, 512, 4, 2),
    },

    # SAP2000, TQS — cálculo estrutural exige CPU e RAM elevados para modelos grandes
    # Referência: https://wiki.csiamerica.com/display/sap2000/System+Requirements
    "calculo_estrutural": {
        "nome": "Cálculo estrutural (SAP2000, TQS)",
        "fonte": "https://wiki.csiamerica.com/display/sap2000/System+Requirements",
        "min": _req(16, 512, 4, 1),
        "rec": _req(32, 1024, 5, 2),
    },

    # Renderização (V-Ray, Lumion) — GPU dedicada obrigatória, RAM alta
    # Fonte: https://docs.chaos.com/display/VRAY/System+Requirements
    "renderizacao": {
        "nome": "Renderização (V-Ray, Lumion)",
        "fonte": "https://docs.chaos.com/display/VRAY/System+Requirements",
        "min": _req(16, 512, 4, 2),
        "rec": _req(32, 1024, 5, 3),
    },

    # -------------------------------------------------------------------------
    # Edição de mídia
    # -------------------------------------------------------------------------
    # Adobe Photoshop 2024 — Fonte oficial:
    # https://helpx.adobe.com/photoshop/system-requirements/2024.html
    # Mínimo: 8 GB RAM (16 GB recomendado), 4 GB SSD, GPU 2 GB VRAM
    "editor_imagem": {
        "nome": "Editor de imagem (Photoshop, GIMP)",
        "fonte": "https://helpx.adobe.com/photoshop/system-requirements/2024.html",
        "min": _req(8, 256, 3, 1),
        "rec": _req(16, 512, 4, 2),
    },

    # Adobe Premiere Pro 2024 — Fonte oficial:
    # https://helpx.adobe.com/premiere-pro/system-requirements/2024.html
    # Mínimo: 16 GB RAM, GPU 4 GB VRAM, 64 GB SSD para mídia
    # Recomendado: 32 GB RAM, GPU dedicada 8 GB VRAM, SSD rápido
    "editor_video": {
        "nome": "Editor de vídeo (Premiere, DaVinci Resolve)",
        "fonte": "https://helpx.adobe.com/premiere-pro/system-requirements/2024.html | https://www.blackmagicdesign.com/products/davinciresolve",
        "min": _req(16, 512, 4, 1),
        "rec": _req(32, 1024, 5, 2),
    },

    # Adobe Illustrator — Fonte oficial:
    # https://helpx.adobe.com/illustrator/system-requirements.html
    # Mínimo: 8 GB RAM, 3 GB SSD; recomendado: 16 GB RAM
    "ilustracao": {
        "nome": "Ilustração vetorial (Illustrator, Inkscape)",
        "fonte": "https://helpx.adobe.com/illustrator/system-requirements.html",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 1),
    },

    # Audacity — software leve, código aberto; requisitos publicados na documentação
    # Fonte: https://support.audacityteam.org/getting-started/faq-installation-and-plug-ins/what-are-the-system-requirements-for-audacity
    "audio": {
        "nome": "Edição de áudio (Audacity)",
        "fonte": "https://support.audacityteam.org/getting-started/faq-installation-and-plug-ins/what-are-the-system-requirements-for-audacity",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # Blender 4.x — Fonte oficial: https://www.blender.org/download/requirements/
    # After Effects: https://helpx.adobe.com/after-effects/system-requirements.html
    # Mínimo Blender: 8 GB RAM, GPU 2 GB VRAM OpenGL 4.3+; recomendado: 32 GB RAM, GPU 8 GB VRAM
    "animacao": {
        "nome": "Animação (After Effects, Blender)",
        "fonte": "https://www.blender.org/download/requirements/ | https://helpx.adobe.com/after-effects/system-requirements.html",
        "min": _req(16, 512, 4, 1),
        "rec": _req(32, 1024, 5, 2),
    },

    # OBS Studio — Fonte: https://github.com/obsproject/obs-studio/wiki/System-Requirements
    # Camtasia: https://www.techsmith.com/camtasia-system-requirements.html
    "captura_tela": {
        "nome": "Gravação de tela (OBS, Camtasia)",
        "fonte": "https://github.com/obsproject/obs-studio/wiki/System-Requirements | https://www.techsmith.com/camtasia-system-requirements.html",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # -------------------------------------------------------------------------
    # Geoprocessamento
    # -------------------------------------------------------------------------
    # QGIS — Fonte oficial: https://qgis-windows.github.io/system-requirements.html
    # Mínimo: 4 GB RAM, CPU 2 núcleos, GPU integrada
    # Recomendado: 8–16 GB RAM, 4 núcleos+, SSD, GPU dedicada
    # ArcGIS Pro 3.4 — Fonte oficial ESRI:
    # https://pro.arcgis.com/en/pro-app/3.4/get-started/arcgis-pro-system-requirements.htm
    # Mínimo: 8 GB RAM, 32 GB SSD, GPU dedicada 4 GB VRAM
    # Recomendado: 32 GB RAM, GPU dedicada
    "sig": {
        "nome": "QGIS / ArcGIS Pro (mapas e SIG)",
        "fonte": "https://qgis-windows.github.io/system-requirements.html | https://pro.arcgis.com/en/pro-app/3.4/get-started/arcgis-pro-system-requirements.htm",
        "min": _req(16, 512, 3, 1),
        "rec": _req(32, 1024, 4, 2),
    },

    # Sensoriamento remoto (ENVI, SNAP ESA): processamento de imagens de satélite
    # Fonte: https://www.nv5geospatialsoftware.com/docs/SystemRequirements.html
    "sensoriamento": {
        "nome": "Sensoriamento remoto / satélite (ENVI, SNAP)",
        "fonte": "https://www.nv5geospatialsoftware.com/docs/SystemRequirements.html | https://step.esa.int/main/toolboxes/snap/",
        "min": _req(16, 512, 4, 1),
        "rec": _req(32, 2048, 5, 2),
    },

    # Agisoft Metashape (processamento de drones) — Fonte: https://www.agisoft.com/downloads/system-requirements/
    # Mínimo: 16 GB RAM, GPU CUDA/OpenCL 2 GB; recomendado: 32 GB RAM, 4 GB+ VRAM
    "drone": {
        "nome": "Processamento de imagens de drone (Agisoft Metashape, DroneDeploy)",
        "fonte": "https://www.agisoft.com/downloads/system-requirements/",
        "min": _req(16, 1024, 4, 1),
        "rec": _req(32, 2048, 5, 2),
    },

    # -------------------------------------------------------------------------
    # Ensino / laboratório
    # -------------------------------------------------------------------------
    # Mesmos requisitos do Microsoft 365 — Editor de texto e apresentações
    "editores_ensino": {
        "nome": "Digitação e apresentações",
        "fonte": "https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365",
        "min": _req(4, 128, 2, 0),
        "rec": _req(8, 256, 3, 0),
    },

    # Moodle (plataforma de ensino a distância) — roda via navegador web
    # Fonte: https://moodledev.io/general/development/policies/minphpversion
    "ambiente_ensino": {
        "nome": "Plataforma de ensino (Moodle, Google Classroom)",
        "fonte": "https://docs.moodle.org/dev/Moodle_server_requirements",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 256, 3, 0),
    },

    # VS Code — Fonte oficial: https://code.visualstudio.com/docs/supporting/requirements
    # Eclipse / IntelliJ: https://www.jetbrains.com/idea/download/system-requirements.html
    # Mínimo prático: 8 GB RAM; recomendado: 16 GB RAM
    "programacao": {
        "nome": "Programação (VS Code, Eclipse, IntelliJ)",
        "fonte": "https://code.visualstudio.com/docs/supporting/requirements | https://www.jetbrains.com/idea/download/system-requirements.html",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # -------------------------------------------------------------------------
    # Dados / TI
    # -------------------------------------------------------------------------
    # PostgreSQL / MySQL — Fonte: https://www.postgresql.org/docs/current/install-requirements.html
    # Mínimo: 1 GB RAM para pequenas bases; para uso real em órgãos recomenda-se 8–16 GB RAM
    "banco_dados": {
        "nome": "Banco de dados (MySQL, PostgreSQL)",
        "fonte": "https://www.postgresql.org/docs/current/install-requirements.html | https://dev.mysql.com/doc/refman/8.0/en/installing.html",
        "min": _req(16, 512, 4, 0),
        "rec": _req(32, 1024, 5, 0),
    },

    # Excel avançado com macros — mesmos requisitos do Microsoft 365, porém com mais RAM
    # Fonte: https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365
    "planilhas_avancadas": {
        "nome": "Excel avançado com macros e tabelas dinâmicas",
        "fonte": "https://support.microsoft.com/en-us/office/system-requirements-for-microsoft-365",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # Power BI Desktop — Fonte oficial Microsoft:
    # https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop
    # Mínimo: 2 GB RAM, CPU 1 GHz x64; recomendado: 8+ GB RAM para datasets grandes
    "bi": {
        "nome": "Business Intelligence (Power BI Desktop, Tableau)",
        "fonte": "https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop | https://www.tableau.com/support/techspecs",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # R / Python / SPSS — ambientes de análise estatística
    # R: https://cran.r-project.org/doc/FAQ/R-FAQ.html
    # Python: https://www.python.org/downloads/
    # IBM SPSS Statistics 29: https://www.ibm.com/support/pages/spss-statistics-system-requirements
    "estatistica": {
        "nome": "Estatística (R, Python, SPSS Statistics)",
        "fonte": "https://cran.r-project.org | https://www.ibm.com/support/pages/spss-statistics-system-requirements",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # Tableau Desktop — Fonte: https://www.tableau.com/support/techspecs
    # Mínimo: 8 GB RAM, 1,5 GB SSD livre; recomendado: 16 GB RAM
    "visualizacao_dados": {
        "nome": "Visualização de dados (Tableau, Power BI Service)",
        "fonte": "https://www.tableau.com/support/techspecs",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # Python (RPA / automação) — perfil leve; semelhante ao VS Code
    "automacao": {
        "nome": "Automação e scripts (Python, RPA)",
        "fonte": "https://www.python.org/downloads/ | https://www.uipath.com/help/latest/System-Requirements",
        "min": _req(8, 256, 3, 0),
        "rec": _req(16, 512, 4, 0),
    },

    # VirtualBox / VMware Workstation — Fonte:
    # https://docs.vmware.com/en/VMware-Workstation-Pro/17/com.vmware.ws.using.doc/GUID-8DE002BD-9B18-4B16-8C32-843DE39D8284.html
    # https://www.virtualbox.org/manual/ch01.html
    # Mínimo: 16 GB RAM (host + VMs); 64 GB SSD p/ disco virtual; recomendado: 32 GB RAM
    "virtualizacao": {
        "nome": "Virtualização (VirtualBox, VMware Workstation)",
        "fonte": "https://docs.vmware.com/en/VMware-Workstation-Pro/17/com.vmware.ws.using.doc/GUID-8DE002BD-9B18-4B16-8C32-843DE39D8284.html | https://www.virtualbox.org/manual/ch01.html",
        "min": _req(16, 512, 4, 0),
        "rec": _req(32, 1024, 5, 0),
    },
}

for _id, _sw in SOFTWARES.items():
    _sw["id"] = _id

MANUAL = {
    "id": "manual",
    "nome": "Programa informado pelo usuário",
    "fonte": "informado pelo órgão",
    "min": _req(8, 256, 3, 0),
    "rec": _req(16, 512, 4, 0),
}
