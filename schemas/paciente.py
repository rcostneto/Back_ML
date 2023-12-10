from typing import List
from pydantic import BaseModel
# import json
# from sqlalchemy import values
from model.paciente import Paciente
# import numpy as np
# import re


class PacienteSchema(BaseModel):
    """ Define como modelo padrao caso nao seja inserido um novo usuario.
    """
    # id: int = 1
    nome_usuario: str = 'Teste'
    age: int = 'qualquer'
    sex: int = 'masc'
    chest_pain: int = 'zero'
    resting_blood_pressure: float = '100'
    cholesterol: float = '200'
    fasting_blood_glucose: int = '100'
    ecg_rest: int = '1'
    maximum_fcm: float = '100'
    


class PacienteBuscaSchema(BaseModel):
    """ Define a estrutura de pesquisa(busca) deve ser representada. Que será
        feita apenas com base no id do paciente.
    """
    id: int


class ListagemPacienteSchema(BaseModel):
    """ Define como uma listagem de pacientes será retornada.
    """
    pacientes:List[PacienteSchema]


def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteSchema.
    """
    result = []
    for paciente in pacientes:   
        result.append({
            "id": paciente.id,
            "nome_usuario": paciente.nome_usuario,
            "age": paciente.age,
            "sex": paciente.sex,
            "chest_pain": paciente.chest_pain,
            "resting_blood_pressure": paciente.resting_blood_pressure,
            "cholesterol": paciente.cholesterol,
            "fasting_blood_glucose": paciente.fasting_blood_glucose,
            "ecg_rest": paciente.ecg_rest,
            "maximum_fcm": paciente.maximum_fcm,
            "result": paciente.result
        })

    return {"pacientes": result}


#def aprensenta_resultado():
    
#    for usuario, veiculo in resultado:
#        print(usuario.nome, veiculo.nome_veiculo)


class PacienteViewSchema(BaseModel):
    """ Define um modelo de como o paciente sera representado.
    """

    id: int = 1
    nome_usuario: str = 'Teste'
    age: int = 'qualquer'
    sex: int = 'masc'
    chest_pain: int = 'zero'
    resting_blood_pressure: float = '100'
    cholesterol: float = '200'
    fasting_blood_glucose: int = '100'
    ecg_rest: int = '1'
    maximum_fcm: float = '100'
    result: float = None
    


class PacienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    # message: str
    id: int

def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "nome_usuario": paciente.nome_usuario,
        "age": paciente.age,
        "sex": paciente.sex,
        "chest_pain": paciente.chest_pain,
        "resting_blood_pressure": paciente.resting_blood_pressure,
        "cholesterol": paciente.cholesterol,
        "fasting_blood_glucose": paciente.fasting_blood_glucose,
        "ecg_rest": paciente.ecg_rest,
        "maximum_fcm": paciente.maximum_fcm,
        "result": paciente.result
    }
