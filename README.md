# Minha API HEART DISEASES


Este projeto foi pensado em uma avaliar e identificar problemas cardíacos de pacientes com base na construção do algoritimo ML(Machine learning).
É efetuado também um teste unitário.

```
    Foi utilizado vários algoritimos do modelo de classificação como(LogisticRegression, KNeighborsClassifier, GaussianNB, SVM(SVC), VotingClassifier, DecisionTreeClassifier, BaggingClassifier, ExtraTreesClassifier), onde o escolhido foi KNN(KNeighborsClassifier) por apresentar melhor acurácia. A forma de inserção de dados para avaliar o paciente estão no arquivo paciente.py dentro da pasta model.
```
Logo abaixo informa como executar a API.


## Como executar 

Após efetuar o download do repositório e com o VSCode aberto, abra a pasta Gerenciamento peças oficina, clicando em Arquivo/Abrir Pasta.
Em seguida clique com o botao direio do mouse em backend e com o esquerdo Abrir no Terminal Integrado.

> Não é obrigatório mas será recomendado usar o virtualenv, uma vez que o projeto foi elaborado com essa ferramenta.
 [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Digite o comando abaixo no terminal para instalar o virtualenv
```
python3 -m venv env
```

Com o env instalado agora iremos ativá-lo.
```
./env/Scripts/activate
```

agora iremos instalar todas as libs/bibliotecas python listadas no `requirements.txt` instaladas.
```
(env)$ pip install -r requirements.txt
```
>*Após instalar as libs é recomendado que faça uma atualização do comando* `pip`
>>python.exe -m pip install --upgrade pip

Execute o comando abaixo para iniciar o serviço
```
    flask run --host 0.0.0.0 --port 5000
```

Comando para sair do serviço
```
    CTRL + C
```

### *Como usar*

>OBS
Logo após a execução da API, uma página com a documentação será aberta em Swagger, Redoc ou RapiDoc, nesse exemplo falaremos da Swagger que servirá para a restante, pois o propósito delas são o mesmo. Foram impementadas 3 rotas.
---

#### **POST/paciente**

Adiciona uma predição dos dados do paciente e salva no banco.

```
Clique em "Try it out", em seguida preencha os campos, depois clique em execute para adicionar os dados do paciente.
```

>Obs: Após o ML efetuar a análise, *Os dados serão adicionados ao banco* e será exibida a confirmação ou erro tanto via terminal quanto swagger.

>Cod:200 - Adicionando paciente.
>Cod:409 - Esse paciente ja existe no banco.
>Cod:400 - O paciente não foi salvo no banco.
---

#### **DELETE/paciente**

Deleta uma paciente a partir do id informado

```
Clique em "Try it out", em seguida escolha o id, depois clique em execute para deletar os dados do paciente.
```

>Obs: *Os dados serão deletados do banco* e será exibida a confirmação ou erro tanto via terminal quanto swagger.

>Cod:200 - Paciente foi removido.
>Cod:404 - Paciente não foi encontrado no banco.
---

#### **GET/pacientes**

Com o Swagger aberto iremos a procura da rota GET/pacientes.
```
Clique em "Try it out", em seguida, clique em execute para buscar dados dos pacientes.
```

>Obs: *Os dados serão salvos no banco* com essa menssagem de confirmação via terminal e swagger.

>Cod:200 - Não há pacientes cadastrados, retornará uma [].
>Cod:200 - pacientes encontrados.

---

# TESTE UNITÁRIO

Esse teste tem por objetivo comparar a acurácia do modelo de classificação feito tanto no COLAB quanto no JUPYTER, com o modelo avaliador do teste.

```
OBS: Para execução do teste, primeiro devemos ativar o virtual env, caso ele ja esteja ativado ignore essa mensagem.
```
Com o env ativado digite o comando listado abaixo para efetuar o teste unitário

> pytest -v test_modelos.py

### Resultado

Nesse teste foi definido que a acurácia mínima é de 72%.

> acurácia menor que 72% FAILED
> acurácia maior que 72% PASSED










