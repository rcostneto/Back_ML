import numpy as np
import pickle


class Model:
    def carrega_modelo(path):
        """ Se o formato for .pkl carrega o arquivo, caso contrario o formato n e suportado.
        """
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('O formato do arquivo e invalido')
        return model
    
    def preditor(model, form):
        """
        Realiza a predicao do paciente atravez do modelo pronto.
        """
        X_input = np.array([form.age,                          
                            form.sex,
                            form.chest_pain,
                            form.resting_blood_pressure,
                            form.cholesterol,
                            form.fasting_blood_glucose,
                            form.ecg_rest,
                            form.maximum_fcm
                ])
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])