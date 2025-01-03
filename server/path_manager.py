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

def get_templates_path():
    return join_path(join_path(get_path(),"server"),"templates")

def file_exists(path):
    if path.exists():
        return True
    else:
        return False
