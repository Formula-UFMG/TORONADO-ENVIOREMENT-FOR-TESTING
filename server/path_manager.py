import os

def join_path(path,folder_file):
    return os.path.join(path,folder_file)

def get_path():
    return os.getcwd()

def get_upload_path():
    raiz_projeto = get_path()
    server = join_path(raiz_projeto, "server")
    static = join_path(server, "static")
    upload = join_path(static, "upload")
    circuitos = join_path(upload, "circuitos")
    return circuitos

def get_documentos_path():
    raiz_projeto = get_path()
    server = join_path(raiz_projeto, "server")
    static = join_path(server, "static")
    upload = join_path(static, "upload")
    documentos = join_path(upload, "documentos")
    return documentos

def get_briefing_path():
    documentos = get_documentos_path()
    briefing = join_path(documentos,"briefing")
    return briefing

def get_debriefing_path():
    documentos = get_documentos_path()
    debriefing = join_path(documentos, "debriefing")
    return debriefing

def get_templates_path():
    raiz_projeto = get_path()
    server = join_path(raiz_projeto, "server")
    templates = join_path(server, "templates")
    return templates

def file_exists(path):
    if path.exists():
        return True
    else:
        return False
