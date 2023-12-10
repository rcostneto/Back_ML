from sqlalchemy import Column, String, Integer, Float

from model import Base

class Paciente(Base):
    __tablename__ = 'paciente'

    id = Column("pk_paciente", Integer, primary_key=True)
    nome_usuario = Column("Paciente", String(20))
    age = Column("Idade", Integer)
    sex = Column("Sexo", Integer)
    chest_pain = Column("Dor no Peito", Integer)
    resting_blood_pressure = Column("Pressao Arterial", Float)
    cholesterol = Column("Colesterol", Float)
    fasting_blood_glucose = Column("Glicose", Integer)
    ecg_rest = Column("ECG", Integer)
    maximum_fcm = Column("FCM", Float)
    result = Column("Diagnostic", Float, nullable=True)




    def __init__(self, nome_usuario:str, age:int, sex:int, 
                 chest_pain:int, resting_blood_pressure:float, 
                 cholesterol:float, fasting_blood_glucose:int, ecg_rest:int,
                 maximum_fcm:float, result:float):
        """
        Cria um Paciente

        Arguments:
            
            nome: nome do paciente.
            idade: idade do paciente.
            sexo: sexo do paciente(0 = masculino, 1 = feminino).
            dor_toraxica: dor no peito, (0 = assintomático, 1 = sintomático).
            PressaoArt_Repouso: pressão arterial(mm Hg) medida em repouso (na admissão ao hospital) 
            colesterol: valor do colesterol sérico em mg/dl
            glicemia_jejum: valor da glicemia aferida em jejum(0 <= 120mg/dl, 1 >= 120mg/dl)
            ecg_repouso: eletrocardiograma em repouso (0 = sem alterações, 1 = alterado)
            fcm: frequência cardíaca máxima alcançada
            resultado: resultado onde (1 = possui doênças cardíacas, 0 = ausência de doênças cardiovasculares)
        """
        self.nome_usuario = nome_usuario
        self.age = age
        self.sex = sex
        self.chest_pain = chest_pain
        self.resting_blood_pressure = resting_blood_pressure
        self.cholesterol = cholesterol
        self.fasting_blood_glucose = fasting_blood_glucose
        self.ecg_rest = ecg_rest
        self.maximum_fcm = maximum_fcm
        self.result = result