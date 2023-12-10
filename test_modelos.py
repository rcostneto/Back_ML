from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciando as Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Dados
url_dados = 'data\Cleveland_golden.csv'
colunas = ['age', 'sex', 'chest_pain', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_glucose', 'ecg_rest', 'maximum_fcm', 'restult']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separar dados de entrada e saida
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]

# Metodo para testar o modelo KNN pelo arquivo Cleveland_golden.csv
def test_modelo_knn():
    # Importando o modelo KNN
    knn_path = 'ml_model\KNN.pkl'
    modelo_knn = Model.carrega_modelo(knn_path)

    #Obtendo as metricas do KNN
    acuracia_knn = avaliador.avaliar(modelo_knn, X, Y)

    # Testar a metrica do KNN
    assert acuracia_knn >= 0.72

# codigo para rodar o pytest
# pytest test_modelos.py ou 
# pytest -v test_modelos.py

