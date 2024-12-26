from classes.membros import Membros

def test_membro():

    membro = Membros(email="teste@email.com", senha="12345", nome="João", subgrupo="Data")

    assert membro.email == "teste@email.com"
    assert membro.senha == "12345"
    assert membro.nome == "João"
    assert membro.subgrupo == "Data"

def test_modifica_membro():

    membro = Membros(email="teste@email.com", senha="12345", nome="João", subgrupo="Data")
    membro.modifica(nome="Isadora", subgrupo="Eletrônica", senha="6789")

    #Verifica se as alterações ocorreram com sucesso
    assert membro.nome == "Isadora"
    assert membro.subgrupo == "Eletrônica"
    assert membro.senha == "6789"

def test_modifica_sem_senha(): #Teste sem modificar a senha

    membro = Membros(email="teste@email.com", senha="12345", nome="João", subgrupo="Data")
    membro.modifica(nome="José", subgrupo="Mecânica", senha=None)

    #Verifica se as alterações ocorreram com sucesso
    assert membro.nome == "José"
    assert membro.subgrupo == "Mecânica"
    assert membro.senha == "12345"

