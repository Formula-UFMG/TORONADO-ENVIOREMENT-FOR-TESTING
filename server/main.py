import os
import sys

from flask import Flask, render_template, redirect, request, session, flash, jsonify
from werkzeug.utils import secure_filename
from datetime import date, datetime
import json

from database import aerodinamica as bd_aerodinamica
from database import chassi as bd_chassi
from database import circuito as bd_circuito
from database import comentario as bd_comentario
from database import dinamica as bd_dinamica
from database import fator_externo as bd_fator_externo
from database import freio as bd_freio
from database import grafico as bd_grafico
from database import log as bd_log
from database import marcacao as bd_marcacao
from database import membros as bd_membros
from database import metodologia as bd_metodologia
from database import motor as bd_motor
from database import piloto as bd_piloto
from database import presenca as bd_presenca
from database import prototipo as bd_prototipo
from database import sensores as bd_sensores
from database import teste as bd_teste
from database import transmissao as bd_transmissao

from server.classes import aerodinamica as cl_aerodinamica
from server.classes import chassi as cl_chassi
from server.classes import circuito as cl_circuito
from server.classes import comentario as cl_comentario
from server.classes import dinamica as cl_dinamica
from server.classes import fator_externo as cl_fator_externo
from server.classes import freio as cl_freio
from server.classes import grafico as cl_grafico
from server.classes import log as cl_log
from server.classes import marcacao as cl_marcacao
from server.classes import membros as cl_membros
from server.classes import metodologia as cl_metodologia
from server.classes import motor as cl_motor
from server.classes import piloto as cl_piloto
from server.classes import presenca as cl_presenca
from server.classes import prototipo as cl_prototipo
from server.classes import sensores as cl_sensores
from server.classes import teste as cl_teste
from server.classes import transmissao as cl_transmissao
from server.classes import objetivos as cl_objetivos 
from server.classes import prototipos_saida as cl_prototipo_saida

import formatter
import path_manager
import error_reporter
import TRMP


app = Flask(__name__, template_folder="templates")
app.secret_key = "FormulaUFMG"

# index, login, inicio, sair
@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email") 
        senha = request.form.get("senha") 
        senha = formatter.encode_password(senha)
        verificado, var_login = bd_membros.login(email,senha)
        if verificado == True and var_login == True:
            session["name"] = email
            return redirect("/inicio")
        elif verificado == True and var_login == False:
            flash("Erro na senha ou no email")
            error_reporter.incorrect_access(email)
            return redirect("/login")
        elif verificado == False:
            flash("Estamos com problemas com integração com o banco de dados, tente mais tarde")
            error_reporter.incorrect_access(email)
            return redirect("/login")
    else:
        return render_template("login.html")

@app.route("/inicio")
def inicio():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_membro, usuario = bd_membros.get_membro(session.get("name"))
        if verificador_membro == True:
            if usuario.subgrupo == "Data Analysis" or usuario.subgrupo == "Gestão" or usuario.subgrupo == "Capitania":
                subgrupo = True
            else:
                subgrupo = False
        return render_template("inicio.html", subgrupo = subgrupo)

@app.route("/sair")
def sair():
    session["name"] = None
    return redirect("/")

# membros
@app.route("/membros")
def membros():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador, membros = bd_membros.get_membros()
        verificador_membro, usuario = bd_membros.get_membro(session.get("name"))
        if verificador == True and verificador_membro == True:
            if usuario.subgrupo == "Data Analysis" or usuario.subgrupo == "Gestão" or usuario.subgrupo == "Capitania":
                subgrupo = True
            else:
                subgrupo = False
            return render_template("membros.html", membros = membros, subgrupo = subgrupo)
        else:
            flash("Erro ao realizar a busca no banco de dados")
            return redirect("/inicio")

@app.route("/set_piloto", methods=["POST", "GET"])
def set_piloto():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            email = request.form.get("email_piloto")
            piloto = cl_piloto.Pilotos(None, formatter.get_temporada(), 0, email, 0)
            verificador, var_piloto = bd_piloto.creat_piloto(piloto)
            if verificador == True and var_piloto == True:
                flash("Mofificado para piloto")
            elif verificador == True and var_piloto == False:
                flash("Esse membro já é um piloto")
            else:
                flash("Erro ao se conectar com o banco de dados")
            return redirect("/membros")
        else:
            return redirect("/membros")

@app.route("/modifica_conta", methods=["POST", "GET"])
def modifica_conta():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            nome = request.form.get("nome_editar")
            subgrupo = request.form.get("subgrupo_editar")
            email = request.form.get("email_editar")
            senha = request.form.get("senha_editar")
            senha_conf = request.form.get("senha_conf_editar")
            if senha == "" and senha_conf == "":
                senha = None
            elif senha != senha_conf:
                flash("senhas diferentes")
                return redirect("/membros")
            else:
                senha = formatter.encode_password(senha)
            verificador, membro = bd_membros.get_membro(email)
            if verificador == True:
                membro.modifica(nome, subgrupo, senha)
                verificador_modfica, var_membro = bd_membros.modifica(membro)
                if verificador_modfica == True and var_membro == True:
                    flash("informaçoes atualizadas")
                elif verificador_modfica == True and var_membro == False:
                    flash("Erro ao atualizar as informações")
                else:
                    flash("Estamos com problemas na integração com o banco de dados")
                return redirect("/membros")
            else:
                flash("Erro ao realizar a busca das informações do membro")
                return redirect("/inicio")
        else:
            return redirect("/membros")

@app.route("/apagar_membro", methods=["POST", "GET"])
def apagar_membro():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            email = request.form.get("email_apagar")
            verificador, membro = bd_membros.get_membro(email)
            if verificador == True:
                verificador, var_membro = bd_membros.apagar(membro)
                if verificador == True and var_membro == True:
                    flash("informações apagadas")
                else:
                    flash("Erro ao apagar o registro")
                return redirect("/membros")
            else:
                flash("Erro ao coletar as informações")
                return redirect("/membros")
        else:
            return redirect("/membros")

@app.route("/cria_membro", methods=["POST", "GET"])
def cria_membro():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            nome = request.form.get("nome")
            subgrupo = request.form.get("subgrupo")
            email = request.form.get("email")
            senha = request.form.get("senha")
            senha_conf = request.form.get("senha_conf")
            if senha != senha_conf or senha == "" or senha_conf == "":
                flash("Senhas diferentes ou com valores nulos")
                return redirect("/inicio")
            else:
                senha = formatter.encode_password(senha)
                membro = cl_membros.Membros(email, senha, nome, subgrupo)
                verificador, var_membro = bd_membros.creat_membro(membro)
                if verificador == True and var_membro == True:
                    flash("usuario cadastrado")
                else:
                    flash("erro ao cadastrar um membro")
                return redirect("/membros")
        else:
            return redirect("/inicio")

# prototipos 
@app.route("/prototipos")
def prototipos():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador, prototipos = bd_prototipo.get_prototipos()
        verificador_membro, usuario = bd_membros.get_membro(session.get("name"))
        if verificador == True and verificador_membro == True:
            if usuario.subgrupo == "Data Analysis" or usuario.subgrupo == "Gestão" or usuario.subgrupo == "Capitania":
                subgrupo = True
            else:
                subgrupo = False
            return render_template("prototipos.html", prototipos=prototipos, subgrupo = subgrupo)
        else:
            flash("Estamos com ploblemas com a comunicação com o banco de dados")
            return redirect("/inicio")

@app.route("/modifica_prototipo", methods=["POST", "GET"])
def modifica_prototipo():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id = request.form.get("id_edicao")
            nome = request.form.get("nome_edicao")
            ano_fabricacao = request.form.get("ano_fabricacao_edicao")
            status = request.form.get("status_edicao")
            peso = request.form.get("peso_edicao")
            temporada = request.form.get("temporada_edicao")
            verificador, prototipo = bd_prototipo.get_prototipo(id)
            if verificador == True:
                prototipo.modificar(nome, ano_fabricacao, status, peso, temporada, None)
                verificador_modifica, var_prototipo = bd_prototipo.modifica(prototipo)
                if verificador_modifica == True and var_prototipo == True:
                    flash("informações atualizadas")
                else:
                    flash("erro ao modificar as informações")
                return redirect("/prototipos")
            else:
                flash("Erro ao coletar as informações do prototipo")
                return redirect("/prototipos")
        else:
            return redirect("/inicio")

@app.route("/apagar_prototipo",  methods=["POST", "GET"])
def apagar_prototipo():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_prototipo = request.form.get("id_apagar")
            verificador, prototipo = bd_prototipo.get_prototipo(id_prototipo)
            if verificador == True:
                verificador, var_prototipo = bd_prototipo.apagar(prototipo)
                if verificador == True and var_prototipo == True:
                    flash("Informação apagada")
                else:
                    flash("Erro ao apagar os registros do prototipo")
                return redirect("/prototipos")
            else:
                flash("Erro ao coletas as informações do banco de dados")
                return redirect("/inicio")
        else:
            return redirect("/inicio")

@app.route("/criar_prototipo", methods=["POST", "GET"])
def criar_prototipo():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            nome = request.form.get("nome")
            ano_fabricacao = request.form.get("ano_fabricacao")
            status = request.form.get("status")
            peso = request.form.get("peso")
            temporada = request.form.get("temporada")
            if formatter.verifica_formatacao_temporada(temporada) == False:
                flash("Formatação da temporada diferenda do padrao esperado")
                return redirect("/prototipos")
            else:
                prototipo = cl_prototipo.Prototipo(None, nome, ano_fabricacao, status, peso, temporada, 0)
                verificador, var_prototipo = bd_prototipo.creat_prototipo(prototipo)
                if verificador == True and var_prototipo == True:
                    flash("prototipo criado")
                else:
                    flash("Erro ao cadadtrar o prototipo")
                return redirect("/prototipos")
        else:
            return redirect("/prototipos")

# circuito
@app.route("/circuito")
def circuito():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador, circuitos = bd_circuito.get_circuitos()
        if verificador == True:
            return render_template("circuitos.html", circuitos = circuitos)
        else:
            return redirect("/inicio")

@app.route("/cria_circuito", methods=["POST", "GET"])
def cria_circuito():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            nome = request.form.get("nome")
            tempo_descolcamento = request.form.get("tempo_descolcamento")
            KM = request.form.get("KM")
            curvas = request.form.get("curvas")
            cones = request.form.get("cones")
            local = request.form.get("local")
            setor = request.form.get("setor")
            data = datetime.today().replace(microsecond=0)
            circuito_ent = cl_circuito.Circuito(None,nome,tempo_descolcamento,KM,curvas,cones,setor,local,data)
            verificador_criacao, var_circuito = bd_circuito.creat_circuito(circuito_ent)
            if verificador_criacao == True and var_circuito == True:
                arquivo = request.files['circuito']
                verificador_id, var_circuito = bd_circuito.get_id(data)
                if verificador_id == True:
                    try:
                        arquivo.save(var_circuito.caminho)
                        flash("registro de circuito realizando")
                        return redirect("/circuito")
                    except Exception as e:
                        flash("informações do circuito cadastradas, porem problemas ao salvar a imagem")
                        error_reporter.report_error(e)
                        return redirect("/inicio")
                else:
                    flash("Erro ao busca as informações ja cadastradas")
                    return redirect("/circuito")
            else:
                flash("Erro ao criar um registro de circuito")
                return redirect("/circuito")
        else:
            return redirect("/circuito")

# Olhar com mais calma depois
@app.route("/modifica_circuito", methods=["POST", "GET"])
def modifica_circuito():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_circuito = request.form.get("id_circuito_editar")
            nome = request.form.get("nome_editar")
            tempo_descolcamento = request.form.get("tempo_descolcamento_editar")
            KM = request.form.get("KM_editar")
            curvas = request.form.get("curvas_editar")
            cones = request.form.get("cones_editar")
            local = request.form.get("local_editar")
            setor = request.form.get("n_setores_editar")
            verificador_circuitos, entidade = bd_circuito.get_circuito(id_circuito)
            if verificador_circuitos == True:
                entidade.modificar(nome, tempo_descolcamento, KM, curvas, cones, setor , local)
                verificador_modifica, var_circuito = bd_circuito.modificar(entidade)
                if verificador_modifica == True and var_circuito == True:
                    flash("informações atualizadas")
                else:
                    flash("Erro ao atualizar as informações")
                    return redirect("/circuito")
                arquivo = request.files['circuito_editar']
                if arquivo.filename != '':
                    try:
                        savePath = entidade.caminho
                        if path_manager.delete_file(savePath) == False:
                            flash("Erro ao substituir a imagem")
                            return redirect("/circuito")
                        else:
                            arquivo.save(savePath)
                            flash("registro de circuito realizando")
                    except Exception as e:
                        flash("informações do circuito cadastradas, porem problemas ao salvar a imagem")
                        error_reporter.report_error(e)
                    finally:
                        return redirect("/circuito")
                else:
                    flash("informações atualizadas, imagem mantida")
                    return redirect("/circuito")
            else:
                flash("Erro ao criar um registro de circuito")
                return redirect("/circuito")
        else:
            return redirect("/circuito")

# Olhar com mais calma depois
@app.route("/apaga_circuito", methods=["POST", "GET"])
def apaga_circuito():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_circuito = request.form.get("id_circuito_apagar")
            verificador, entidade_circuito = bd_circuito.get_circuito(id_circuito)
            if verificador == True:
                verificador_apagar, var_circuito = bd_circuito.apagar(entidade_circuito)
                caminho = entidade_circuito.caminho
                if verificador_apagar == True and var_circuito == True:
                    flash("Registro apagado")
                else:
                    flash("Erro ao apagar um registro")
                if formatter.delete_file(caminho) == True:
                    flash("Imagem apagada")
                else:
                    flash("Erro ao apagar a imagem")
                return redirect("/circuito")
            else:
                flash("Erro ao pegar as informações sobre o circuito")
                return redirect("/circuito")
        else:
            return redirect("/circuito")

# metodologia
@app.route("/metodologia")
def metodologia():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador, entidade_prototipos = bd_prototipo.get_prototipos()
        if verificador == True:
            return render_template("metodologia.html", prototipos = entidade_prototipos)
        else:
            flash("Erro na busca no banco de dados")
            return redirect("/inicio")

@app.route('/metodologia/prototipo', methods=['POST'])
def processar_prototipo_metodologia():
    if not session.get("name"):
        return redirect("/login")
    else:
        data = request.json
        prototipo_id = data.get('id')
        verificador, entidade_prototipo = bd_prototipo.get_prototipo(prototipo_id)
        if verificador == True:
            temporada = entidade_prototipo.temporada
            verificador, lista_entidades = bd_metodologia.get_metodologias_temporada(temporada)
            if verificador == True:
                lista_dicionarios = formatter.formata_classe_dicionario(lista_entidades)
                return jsonify(lista_dicionarios)

@app.route("/cria_metodologia", methods=["POST", "GET"])
def cria_metodologia():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            objetivo = request.form.get("objetivo")
            N_pessoas = request.form.get("N_pessoas")
            subgrupo = request.form.get("subgrupo")
            procedimento = request.form.get("procedimento")
            N_voltas = request.form.get("N_voltas")
            temporada = request.form.get("temporada")
            if formatter.verifica_formatacao_temporada(temporada) == False:
                flash("Formato da temporada diferente")
                return redirect("/metodologia")
            else:
                metodologia = cl_metodologia.Metodologia(None, objetivo, N_pessoas, subgrupo, procedimento, N_voltas, temporada, "Em aberto")
                verificador, var_metodologia = bd_metodologia.creat_metodologia(metodologia)
                if verificador == True and var_metodologia == True:
                    flash("Metodologia cadastrada")
                else:
                    flash("Erro ao realizar o cadastro de metodologia")
                return redirect("/metodologia")
        else:
            return redirect("/metodologia")

@app.route("/modifica_metodologia", methods=["POST", "GET"])
def modifica_metodologia():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_metodologia = request.form.get("id_metodologia")
            objetivo = request.form.get("objetivo")
            N_pessoas = request.form.get("N_pessoas")
            subgrupo = request.form.get("subgrupo")
            procedimento = request.form.get("procedimento")
            N_voltas = request.form.get("N_voltas")
            verificador, metodologia = bd_metodologia.get_metodologia(id_metodologia)
            if verificador == True:
                metodologia.modificar(objetivo, N_pessoas, subgrupo, procedimento, N_voltas, None)
                verificador_modifica, var_metodologia = bd_metodologia.modificar(metodologia)
                if verificador_modifica == True and var_metodologia == True:
                    flash("informações atualizadas")
                else:
                    flash("Erro ao modificar as informações")
                return redirect("/metodologia")
            else:
                flash("Erro ao buscar as informações")
                return redirect("/metodologia")
        else:
            return redirect("/metodologia")

@app.route("/apaga_metodologia", methods=["POST", "GET"])
def apaga_metodologia():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_metodologia = request.form.get("id_metodologia")
            verificador, metodologia = bd_metodologia.get_metodologia(id_metodologia)
            if verificador == True:
                verificador_apagar, var_metodologia = bd_metodologia.apagar(metodologia)
                if verificador_apagar == True and var_metodologia == True:
                    flash("informação apagada")
                else:
                    flash("Erro ao apagar registro de informação")
                return redirect("/metodologia")
            else:
                flash("Erro ao buscar as informações")
                return redirect("/metodologia")
        else:
            return redirect("/metodologia")

#testa as funções
# testes
@app.route("/teste")
def teste():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_prototipos, prototipos = bd_prototipo.get_prototipos()
        if verificador_prototipos == True:
            return render_template("teste.html", prototipos = prototipos)
        else:
            flash("Erro na busca")
            return redirect("/inicio")

@app.route("/teste/prototipo")
def processar_prototipo_teste():
    if not session.get("name"):
        return redirect("/login")
    else:
        data = request.json
        prototipo_id = data.get('id')
        verificador, lista_testes = bd_teste.get_teste_prototipo(prototipo_id)
        if verificador == True:
            lista_dicionarios = formatter.formata_classe_dicionario(lista_testes)
            return jsonify(lista_dicionarios)

@app.route("/cria_teste", methods=["POST", "GET"])
def cria_teste():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            N_pilotos = request.form.get("contador_piloto")
            nome_caixa_piloto = "caixa_piloto_"
            pilotos = []
            for i in range(int(N_pilotos)):
                if i < 10:
                    nome_caixa = nome_caixa_piloto + str("0") + str(i + 1)
                else:
                    nome_caixa = nome_caixa_piloto + str(i + 1)
                piloto = request.form.get(nome_caixa)
                pilotos.append(formatter.coleta_informacao(piloto))
            pilotos = formatter.concatenar_vetor(pilotos)

            N_objetivos = request.form.get("contador_objetivos")
            nome_caixa_objetivos = "caixa_objetivos_"
            objetivos_id = []
            for i in range(int(N_objetivos)):
                if i < 10:
                    nome_caixa = nome_caixa_objetivos + str("0") + str(i + 1)
                else:
                    nome_caixa = nome_caixa_objetivos + str(i + 1)
                objetivo = request.form.get(nome_caixa)
                objetivos_id.append(formatter.coleta_informacao(objetivo))
            objetivos_id = formatter.concatenar_vetor(objetivos_id)

            data = request.form.get("data")
            inicio_teste = request.form.get("incio")
            inicio_teste = formatter.string_to_datetime(inicio_teste)
            fim_teste = request.form.get("fim")
            fim_teste = formatter.string_to_datetime(fim_teste)
            almoco = request.form.get("almoco")
            if almoco == "on":
                almoco = True
            else:
                almoco = False

            id_prototipo = request.form.get("prototipos")
            id_prototipo = formatter.coleta_informacao(id_prototipo)
            id_circuito = request.form.get("pista")

            teste = cl_teste.Teste(None,pilotos,objetivos_id,0,inicio_teste,fim_teste,almoco,data,id_prototipo, id_circuito, "Em aberto")

            verificador, var_teste = bd_teste.creat_teste(teste)
            if verificador == True and var_teste == True:
                flash("Teste cadastrado")
            elif verificador == True and var_teste == False:
                flash("erro ao cadastrar o teste")
            elif verificador == False:
                flash("Erro ou se conectar com o banco de dados")
            return redirect("/teste")
        else:
            verificador_pilotos, pilotos = bd_piloto.get_pilotos()
            verificador_circuitos,circuitos = bd_circuito.get_circuitos()
            verificador_prototipos, ent_prototipos = bd_prototipo.get_prototipos()
            verificador_metodologia, ent_metodologia = bd_metodologia.get_metodologias()
            objetivos = []
            if verificador_pilotos == True and verificador_prototipos == True and verificador_metodologia == True and verificador_circuitos == True:
                for metodologia in ent_metodologia:
                    objetivos.append(cl_objetivos.Objetivos(metodologia.id_metodologia, metodologia.objetivo, metodologia.status,metodologia.temporada))
                for piloto in pilotos:
                    verificador_membro, ent_membro = bd_membros.get_membro(piloto.email)
                    if verificador_membro == True:
                        piloto.formato_saida(ent_membro.nome)
                prototipos_saida = []
                for ent_prototipo in ent_prototipos:
                    informacoes = str(ent_prototipo.id) + "|" + str(ent_prototipo.temporada)
                    prototipos_saida.append(cl_prototipo_saida.Prototipos(ent_prototipo.nome,informacoes))
                return render_template("cria_teste.html",circuitos = circuitos, pilotos = pilotos, prototipos = prototipos_saida, objetivos = objetivos)
            else:
                return redirect("/teste")

@app.route("/modifica_teste", methods=["POST", "GET"])
def modifica_teste():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_teste  = request.form.get("id_teste")

            N_pilotos = request.form.get("N_pilotos")
            nome_caixa_piloto = "pilotos_"
            pilotos = []
            for i in range(N_pilotos):
                pilotos.append(request.form.get(nome_caixa_piloto + str(i)))
            pilotos = formatter.concatenar_vetor(pilotos)

            N_objetivos = request.form.get("N_objetivos")
            nome_caixa_objetivos = "objetivos_"
            objetivos_id = []
            for i in range(N_objetivos):
                objetivos_id.append(request.form.get(nome_caixa_objetivos + str(i)))
            objetivos_id = formatter.concatenar_vetor(objetivos_id)

            data = request.form.get("data")
            inicio_teste = request.form.get("entrada")
            fim_teste = request.form.get("saida")
            almoco = request.form.get("almoco")

            id_prototipo = bd_prototipo.max_id()
            id_circuito = request.form.get("circuito")

            verificador, entidade_teste = bd_teste.get_teste(id_teste)
            if verificador == True:
                entidade_teste.modifica(pilotos, objetivos_id, inicio_teste, fim_teste, almoco, data, id_prototipo, id_circuito)
                verificador, var_teste = bd_teste.modificar(entidade_teste)
                if verificador == True and var_teste == True:
                    flash("informações atualizadas")
                elif verificador == True and var_teste == False:
                    flash("Erro ao atualizar as informações")
                elif verificador == False:
                    flash("Erro ao se conectar com o banco de dados")
                return redirect("/teste")
        else:
            return redirect("/teste")

@app.route("/apaga_teste", methods=["POST", "GET"])
def apaga_teste():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_teste  = request.form.get("id_apagar")
            verificador, entidade_teste = bd_teste.get_teste(id_teste)
            if verificador == True:
                verificador, var_teste = bd_teste.apagar(entidade_teste)
                if verificador == True and var_teste == True:
                    flash("teste apagado")
                elif verificador == True and var_teste == False:
                    flash("Erro ao apagar")
                elif verificador == False:
                    flash("Erro no contato com o banco de dados")
                return redirect("/teste")
            else:
                flash("erro na busca")
        else:
            return redirect("/teste")

# sensores
@app.route("/sensores", methods=["POST", "GET"])
def sensores():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_prototipos, entidades_prototipos = bd_prototipo.get_prototipos()
        if verificador_prototipos == True:
            return render_template("sensores.html", prototipos = entidades_prototipos)
        else:
            flash("Erro na busca das informações")
            return redirect("/inicio")

@app.route("/sensores/prototipo", methods=['POST'])
def processar_prototipo_sensores():
    if not session.get("name"):
        return redirect("/login")
    else:
        data = request.json
        prototipo_id = data.get('id_prototipo')
        verificador, lista_classes = bd_sensores.get_sensor_prototipo(prototipo_id)
        if verificador == True:
            lista_dicionarios = formatter.formata_classe_dicionario(lista_classes)
            return jsonify(lista_dicionarios)

@app.route("/cria_sensor", methods=["POST", "GET"])
def cria_sensor():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            nome = request.form.get("nome")
            id_prototipo = request.form.get("id_prototipo")
            informacao = request.form.get("informacao")
            sensor = cl_sensores.Sensores(None,nome,id_prototipo,informacao)
            verificador, var_sensor = bd_sensores.creat_sensores(sensor)
            if verificador == True and  var_sensor == True:
                flash("sensor cadastrado")
            elif verificador == True and var_sensor == False:
                flash("Erro no cadastro dos sensores")
            else:
                flash("erro na comunicação com o banco de dados")
            return redirect("/sensores")
        else:
            return redirect("/sensores")

@app.route("/modifica_sensores", methods=["POST", "GET"])
def modifica_sensores():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_sensor = request.form.get("id_editar")
            nome = request.form.get("nome_editar")
            informacao = request.form.get("informacao_editar")
            verificador , sensor = bd_sensores.get_sensor(id_sensor)
            if verificador == True:
                sensor.modificar(nome, informacao)
                verificador, var_sensor = bd_sensores.modificar(sensor)
                if verificador == True and var_sensor == True:
                    flash("informações atualizadas")
                elif verificador == True and var_sensor == False:
                    flash("Erro ao modificarr as informações")
                else:
                    flash("Erro no contato com o banco de dados")
                return redirect("/sensores")
            else:
                flash("Erro ao realizar a busca no banco de dados")
                return redirect("/inicio")
        else:
            return redirect("/sensores")

@app.route("/apagar_sensores", methods=["POST", "GET"])
def apagar_sensores():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_sensor = request.form.get("id_apagar")
            verificador , sensor = bd_sensores.get_sensor(id_sensor)
            if verificador == True:
                verificador, var_sensor = bd_sensores.apagar(sensor)
                if verificador == True and var_sensor == True:
                    flash("informações apagadas")
                elif verificador == True and var_sensor == False:
                    flash("erro ao apagar as informações")
                else:
                    flash("erro na comunicação com o banco de dados")
                return redirect("/sensores")
            else:
                flash("Erro ao realizar buscas")
                return redirect("/inicio")
        else:
            return redirect("/sensores")

# Documentos 
@app.route("/documentos", methods=["POST", "GET"])
def documentos():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_prototipos, entidades_prototipos = bd_prototipo.get_prototipos()
        if verificador_prototipos == True:
            return render_template("documentos.html", prototipos = entidades_prototipos)

@app.route('/documentos/prototipo', methods=['POST'])
def processar_prototipo():
    data = request.json
    prototipo_id = data.get('id')
    verificador_testes, entidade_teste = bd_teste.get_teste_prototipo(prototipo_id)
    if verificador_testes == True:
        lista_dicionarios = formatter.formata_classe_dicionario(entidade_teste)
        return jsonify(lista_dicionarios)

# Log 
@app.route("/log", methods=["POST", "GET"])
def log():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_prototipo, ent_prototipos = bd_prototipo.get_prototipos()
        verificador_pilotos, ent_pilotos = bd_piloto.get_pilotos()
        verificador_teste, ent_testes = bd_teste.get_testes()
        if verificador_prototipo == True and verificador_pilotos == True and verificador_teste == True:
            for ent_teste in ent_testes:
                ent_teste.pilotos = formatter.deserializacao(ent_teste.pilotos,"int")
            return render_template("logs.html", prototipos = ent_prototipos,pilotos=ent_pilotos,testes=ent_testes)
        else:
            return redirect("/inicio")

@app.route("/cria_log/<id_teste>", methods=["POST", "GET"])
def cria_log(id_teste):
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            link = request.form.get("link")
            descricao = request.form.get("descricao")
            piloto = request.form.get("piloto")
            id_teste = request.form.get("test")
            arquivos = request.files.getlist('logs')
            passada = request.form.get("passada")
            for arquivo in arquivos:
                data = datetime.today().replace(microsecond=0)
                entidade = cl_log.Log(link = link, descricao = descricao, id_piloto = piloto, id_teste = id_teste, data = data,passada=passada)
                verificador, var_log = bd_log.cria_log(entidade)
                if verificador == True and var_log == True:
                    verificador, log = bd_log.get_log_data(data)
                    if verificador == True:
                        try:
                            arquivo.save(log.caminho)
                            TRMP.get_informacoe(log)
                        except Exception as e:
                            flash("Erro ao salvar os logs")
                            bd_log.apagar_log(entidade)
                            return redirect("/teste")
                    else:
                        flash("Erro ao buscar as informações")
                        bd_log.apagar_log(entidade)
                        return redirect("/log")
                elif verificador == True and var_log == False:
                    flash("Erro no cadastro do log")
                    return redirect("/log")
                elif verificador == False:
                    flash("Erro no contato com o banco de dados")
                    return redirect("/inicio")
            return redirect("/cria_log/{}".format(id_teste))
        else:
            verificador_teste, entidade_teste = bd_teste.get_teste(id_teste)
            if verificador_teste != True:
                flash("Erro na busca das informação para o cadastro do teste")
                return redirect("/inicio")
            else:
                pilotos = formatter.deserializacao(entidade_teste.pilotos, "int")
                lista_pilotos = []
                for piloto in pilotos:
                    verificador_piloto, entidade_piloto = bd_piloto.get_piloto(piloto)
                    if verificador_piloto == True:
                        verificador_membro, membro = bd_membros.get_membro(entidade_piloto.email)
                        if verificador_membro == True:
                            entidade_piloto.add_nome(membro.nome)
                            lista_pilotos.append(entidade_piloto)
                        else:
                            flash("Erro ao coleetar as informações")
                            return redirect("/inicio")
                    else:
                        flash("Erro ao coleetar as informações")
                        return redirect("/inicio")
                return render_template("cria_log.html", id = id_teste, pilotos = lista_pilotos)

@app.route("/modifica_log", methods=["POST", "GET"])
def modifica_log():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_logs = request.form.get("id_logs")
            link = request.form.get("link")
            descricao = request.form.get("descricao")
            piloto = request.form.get("piloto")
            verificador, entidade = bd_log.get_log(id_logs)
            if verificador == True:
                entidade.modifica(link,descricao,piloto)
                verificador, var_log = bd_log.modifica(entidade)
                if verificador == True and var_log == True:
                    flash("log modificado")
                elif verificador == True and var_log == False:
                    flash("Erro ao modifocar o log")
                elif verificador == False:
                    flash("Erro com o contato com o banco de dados")
                return redirect("/log")
            else:
                flash("Erro ao realizar a busca")
                return redirect("/log")
        else:
            return redirect("/log")

@app.route("/apagar_log", methods=["POST", "GET"])
def apagar_log():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_logs = request.form.get("link")
            verificador, entidade = bd_log.get_log(id_logs)
            if verificador == True:
                verificador, var_log = bd_log.apagar_log(entidade)
                if verificador == True and var_log == True:
                    flash("log apagado")
                elif verificador == True and var_log == False:
                    flash("Erro ao apagar o log")
                elif verificador == False:
                    flash("Erro com o contato com o banco de dados")
                return redirect("/log")
            else:
                flash("Erro ao realizar a busca")
                return redirect("/log")
        else:
            return redirect("/log")

# Piloto 
@app.route("/pilotos", methods=["POST", "GET"])
def pilotos():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_prototipo, entidade_prototipos = bd_prototipo.get_prototipos()
        if verificador_prototipo == True:
            return render_template("pilotos.html", prototipos = entidade_prototipos)
        else:
            return redirect("/inicio")

@app.route("/pilotos/prototipo", methods=['POST'])
def processar_prototipo_pilotos():
    if not session.get("name"):
        return redirect("/login")
    else:
        data = request.json
        prototipo_id = data.get('id_prototipo')
        verificador, entidade_prototipo = bd_prototipo.get_prototipo(prototipo_id)
        if verificador == True:
            verificador, lista_classes = bd_piloto.get_pilotos_temporada(entidade_prototipo.temporada)
            lista_classes = formatter.formata_lista_pilotos(lista_classes)
            if lista_classes == False:
                flash("Erro na formatação das informações")
                return redirect("/inicio")
            else:
                lista_dicionarios = formatter.formata_classe_dicionario(lista_classes)
                return jsonify(lista_dicionarios)

@app.route("/apagar_piloto", methods=["POST", "GET"])
def apagar_piloto():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            id_apagar = request.form.get("id_piloto")
            verificador, entidade_piloto = bd_piloto.get_piloto(id_apagar)
            if verificador == True:
                verificador_apagar, var_apagar = bd_piloto.apagar(entidade_piloto)
                if verificador_apagar == True and var_apagar == True:
                    flash("Registro apagado")
                else:
                    flash("Erro ao apagar o registro")
                return redirect("/pilotos")
            else:
                flash("Erro na coleta das informações")
                return redirect("/inicio")

# TRPM 
@app.route("/trpm_selecao")
def trpm_selecao():
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_prototipo, entidade_prototipo = bd_prototipo.get_prototipos()
        if verificador_prototipo == True:
            return render_template("selecao_log.html", prototipos = entidade_prototipo)
        else:
            flash("Erro ao realizar a busca das informações")
            return redirect("/inicio")

@app.route("/get_teste/<selected_option>",methods=['GET'])
def get_teste(selected_option):
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_teste, entidades_testes = bd_teste.get_teste_prototipo(selected_option)
        if verificador_teste == True:
            entidades_testes_dict = [teste.to_dict() for teste in entidades_testes]
            return jsonify(entidades_testes_dict)
        else:
            flash("Erro ao realizar a busca das informações")
            return redirect("/trpm_selecao")

@app.route("/get_piloto/<selected_teste>", methods=['GET'])
def get_piloto(selected_teste):
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_teste, entidade_teste = bd_teste.get_teste(selected_teste)
        if verificador_teste == True:
            entidade_teste.pilotos = formatter.deserializacao(entidade_teste.pilotos,"int")
            entidade_teste.pilotos = formatter.formatacao_piloto(entidade_teste.pilotos)
            if (isinstance(entidade_teste.pilotos, str))  == True:
                flash(entidade_teste.pilotos)
                return redirect("/trpm_selecao")
            else:
                return jsonify(entidade_teste.pilotos)

@app.route("/get_logs/<selected_piloto>", methods=['GET'])
def get_logs(selected_piloto):
    if not session.get("name"):
        return redirect("/login")
    else:
        teste_id = request.args.get('teste_id', type=int)
        verificador_log, entidade_log = bd_log.get_log_piloto_teste(selected_piloto, teste_id)
        if verificador_log == True:
            lista_dic = []
            for log in entidade_log:
                lista_dic.append(formatter.formatar_select_log(log))
            return jsonify(lista_dic)
        else:
            flash("Erro na coleta das informações")
            return redirect("/trpm_selecao")

@app.route("/get_descricao/<selected_log>", methods=['GET'])
def get_descricao(selected_log):
    if not session.get("name"):
        return redirect("/login")
    else:
        verificador_log, entidade_logs = bd_log.get_log(selected_log)
        if verificador_log == True:
            return jsonify(formatter.formatar_descricao(entidade_logs))
        else:
            flash("Erro na coleta das informações")
            return redirect("/trpm_selecao")

# modificar os nomes dos gets
@app.route("/trpm_coleta", methods=["POST", "GET"])
def trpm_coleta():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            quantidade_blocos = request.form.get("quantidade_blocos")
            lista_dic = []
            for i in range(int(quantidade_blocos)):
                nome = request.form.get("block_name_{}".format(i+1))
                prototipo = request.form.get("select1_{}".format(i+1))
                test = request.form.get("select2_{}".format(i+1))
                piloto = request.form.get("select3_{}".format(i+1))
                logs = request.form.get("select4_{}".format(i+1))
                entidade_dic = {
                    "nome": nome,
                    "prototipo": prototipo,
                    "teste": test,
                    "piloto": piloto,
                    "log":logs
                }
                lista_dic.append(entidade_dic)
            json_string = json.dumps(lista_dic, indent=4)
            data_hora = datetime.now()
            data_hora = str(data_hora)
            data_hora = data_hora.replace("-","")
            data_hora = data_hora.replace(" ","")
            data_hora = data_hora.replace(":","")
            data_hora = data_hora.replace(".","")
            identificador_arquivo = session.get("name") + "_" + data_hora + ".json"
            caminho_json = path_manager.join_path(path_manager.get_json(), identificador_arquivo)
            try:
                with open(caminho_json,"w") as arquivo:
                    json.dump(json_string, arquivo, indent=4)
            except:
                flash("Erro ao salvar as informações para a exibição dos dados")
                return redirect("/trpm_selecao")
            else:
                return redirect(f"/trpm/{data_hora}")
        else:
            return redirect("/inicio")

@app.route("/trpm/<id_json>")
def trpm(id_json):
    if not session.get("name"):
        return redirect("/login")
    else:
        identificador_arquivo = session.get("name") + "_" + id_json + ".json"
        caminho_json = path_manager.join_path(path_manager.get_log(),identificador_arquivo)
        try:
            with open(caminho_json,"r") as arquivo:
                dados = json.load(arquivo)
        except:
            flash("Erro ao realizar a leitura das informações")
        else:
            dados = formatter.formatação_graficos(dados)
        return render_template("trpm.html", dados = dados)

#formatar as informações de coleta
@app.route("/trpm_forms",methods=["POST", "GET"])
def trpm_forms():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            quantidade_marca = request.form.get("quantidade_blocos")
            id_grafico = request.form.get("quantidade_blocos")
            lista_marcacao = []
            for i in range(int(quantidade_marca)):
                ponto_inicial = request.form.get("quantidade_blocos")
                x,y = formatter.formata_coodenadas(ponto_inicial)
                raio_marca = request.form.get("quantidade_blocos")
                comentario = request.form.get("quantidade_blocos")
                cor = request.form.get("quantidade_blocos")
                entidade_marcacao = cl_marcacao.Marcacao(None, x, y, cor, raio_marca, id_grafico, comentario)
                lista_marcacao.append(entidade_marcacao)
            for marcacao in lista_marcacao:
                verificador_marcacao, var_marcacao = bd_marcacao.creat_marcacao(marcacao)
                if verificador_marcacao != True and var_marcacao != True:
                    flash("Erro ao salvar as informações da marcação")
                    return redirect("/trpm_selecao")
                else:
                    flash("marcações salvas no banco de dados")

@app.route("/modifica_creds", methods=["POST", "GET"])
def modifica_creds():
    if not session.get("name"):
        return redirect("/login")
    else:
        if request.method == "POST":
            arquivo = request.files['arquivo']
            caminho = path_manager.get_creds()
            if caminho == False:
                flash("Erro ao apagar a creds antiga")
                error_reporter.report_error("Erro ao apagar a creds antiga")
                return redirect("/inicio")
            try:
                arquivo.save(caminho)
                flash("creds atualizadas")
            except Exception as e:
                flash("Erro ao atualizar as creds")
                error_reporter.report_error(e)
            finally:
                return redirect("/inicio")
        else:
            return render_template("creds.html")

if __name__ == "__name__":
    app.run(debug=True)
#teste de envio
