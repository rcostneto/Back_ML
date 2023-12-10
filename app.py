from asyncore import loop
# import json
from urllib import response
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote
from numpy import indices
import requests
import pprint
import pandas
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from model.__init__ import db_url

from model import Session, Paciente, Model
from logger import logger
from schemas import *
from flask_cors import CORS



info = Info(title="HEART DISEASES", version="1.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adicao, visualizacao e remoção de pacientes a base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo Paciente à base de dados

    Retorna uma representação dos pacientes.
    """
    # Carregando o modelo ML
    ml_path = 'ml_model/KNN.pkl'
    modelo = Model.carrega_modelo(ml_path)

    paciente = Paciente(
        nome_usuario = form.nome_usuario.strip(),
        age = form.age,
        sex = form.sex,
        chest_pain = form.chest_pain,
        resting_blood_pressure = form.resting_blood_pressure,
        cholesterol = form.cholesterol,
        fasting_blood_glucose = form.fasting_blood_glucose,
        ecg_rest = form.ecg_rest,
        maximum_fcm = form.maximum_fcm,
        result = Model.preditor(modelo, form))
    
    logger.debug(f"Adicionando paciente de nome: '{paciente.nome_usuario}'")
    
    try:
        # criando conexão com o banco
        session = Session()
        # adicionando paciente
        session.add(paciente)
        # efetivando o comando de adição de novo paciente na tabela
        session.commit()
        logger.debug(f"Adicionado paciente de nome: '{paciente.nome_usuario}'")
        return apresenta_paciente(paciente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Esse paciente ja existe no banco :/"
        logger.warning(f"Erro ao adicionar o paciente '{paciente.nome_usuario}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "O paciente não foi salvo no banco :/"
        logger.warning(f"Erro ao adicionar o paciente '{paciente.nome_usuario}', {error_msg}")
        return {"mesage": error_msg}, 400
    

@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteDelSchema, "404": ErrorSchema})
def del_paciente(query: PacienteDelSchema):
    """Deleta um Paciente a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    usuario_id = (query.id)
    print(usuario_id)
    logger.debug(f"Deletando dados sobre paciente #{usuario_id}")
    # criando conexão com o banco
    session = Session()
    # fazendo a remoção
    count = session.query(Paciente).filter(Paciente.id == usuario_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletando paciente #{usuario_id}")
        return {"mesage": "Paciente foi removido", "id": usuario_id}
    else:
        # se o paciente não foi encontrado
        error_msg = "Paciente não foi encontrado no banco :/"
        logger.warning(f"Erro ao deletar o paciente #'{usuario_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    

# @app.get('/paciente', tags=[paciente_tag],
#          responses={"200": PacienteViewSchema, "404": ErrorSchema})
# def get_pacientes(query: PacienteBuscaSchema):
#     """Faz a busca por um Paciente a partir do seu nome.

#     Retorna uma representação dos pacientes.
#     """
#     usuario_id = unquote(unquote(query.id))
#     logger.debug(f"Coletando dados sobre usuario #{usuario_id}")
#     # criando conexão com a base
#     session = Session()
#     # fazendo a busca
#     paciente = session.query(Paciente).filter(Paciente.nome_usuario == usuario_id).first()

#     if not paciente:
#         # se o paciente não foi encontrado
#         error_msg = "Paciente não localizado no banco :/"
#         logger.warning(f"Erro ao buscar o paciente '{usuario_id}', {error_msg}")
#         return {"mesage": error_msg}, 404
#     else:
#         logger.debug(f"Pacientes encontrados: '{paciente.nome_usuario}'")
#         # retorna a representação de fornecedor
#         return apresenta_paciente(paciente), 200
    

@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": ListagemPacienteSchema, "404": ErrorSchema})
def get_paciente():
    """Faz a busca por todos os Pacientes cadastrados no banco de dados.

    Retorna uma representação da lista de pacientes.
    """
    
    logger.debug(f"Coletando pacientes ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    pacientes = session.query(Paciente).order_by(Paciente.id.asc()).all()

    if not pacientes:
        # se não há pacientes cadastrados
        return {"pacientes": []}, 200
    else:
        logger.debug(f"%d Pacientes encontrados" % len(pacientes))
        # retorna a representação do paciente
        print(pacientes)
        return apresenta_pacientes(pacientes), 200