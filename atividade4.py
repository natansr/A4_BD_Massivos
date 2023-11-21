from pymongo import MongoClient
from bson.objectid import ObjectId

from bson.objectid import ObjectId
import pandas as pd

# Conectando ao servidor MongoDB (executado via Docker Compose)
client = MongoClient('localhost', 27017, username='root', password='example')

# Acessando o banco de dados 'curso' (cria o banco se não existir)
db = client['curso']

# Listando os bancos de dados existentes
print("Bancos de Dados Existentes:")
print(client.list_database_names())

# Mostrando o banco de dados corrente
print("\nBanco de Dados Corrente:")
print(db)

# Criando uma coleção 'alunos' e inserindo um documento
alunos = db['alunos']
alunos.insert_one({'nome': 'Paulo', 'idade': 29, 'nota': 0})

# Listando os documentos da coleção 'alunos'
print("\nDocumentos da Coleção 'alunos':")
for aluno in alunos.find():
    print(aluno)

# Criando uma lista de alunos para inserção em lote
alunos_list = [
    {'nome': 'Joao', 'idade': 25, 'nota': 8, 'bolsista': True},
    {'nome': 'Maria', 'idade': 23, 'nota': 6, 'bolsista': False},
    {'nome': 'Pedro', 'idade': 22, 'nota': 7, 'bolsista': True},
    {'nome': 'Ana', 'idade': 24, 'nota': 9, 'bolsista': True},
    {'nome': 'Carlos', 'idade': 21, 'nota': 5, 'bolsista': False},
    {'nome': 'Laura', 'idade': 20, 'nota': 8, 'bolsista': True},
    {'nome': 'Fernando', 'idade': 22, 'nota': 6, 'bolsista': False},
    {'nome': 'Julia', 'idade': 23, 'nota': 7, 'bolsista': True},
    {'nome': 'Rafael', 'idade': 24, 'nota': 8, 'bolsista': True},
    {'nome': 'Mariana', 'idade': 21, 'nota': 6, 'bolsista': False},
    {'nome': 'Gabriel', 'idade': 22, 'nota': 9, 'bolsista': True},
    {'nome': 'Sofia', 'idade': 23, 'nota': 5, 'bolsista': False},
    {'nome': 'Lucas', 'idade': 25, 'nota': 7, 'bolsista': True},
]


# Inserindo os alunos em um único comando
alunos.insert_many(alunos_list)




##################PARTE DE IMPORTACAO DO CSV


# Importando de fontes externas (CSV)
# Lendo o arquivo CSV usando pandas
df = pd.read_csv('csv/seu_arquivo.csv')

# Convertendo os dados do DataFrame para uma lista de dicionários
alunos_csv = df.to_dict(orient='records')

# Inserindo os alunos do CSV no banco de dados
alunos.insert_many(alunos_csv)





# Buscando alunos específicos - 1
print("\nBuscando aluno com nome 'Paulo':")
print(alunos.find_one({'nome': 'Paulo'}))

# Buscando alunos específicos - 2
print("\nBuscando aluno com nome 'LukeSkywalker':")
print(alunos.find_one({'nome': 'LukeSkywalker'}))


# Buscando alunos específicos
print("\nBuscando aluno com nome '':")
print(alunos.find_one({'nome': 'Paulo'}))


print("\nBuscando alunos bolsistas:")
for aluno in alunos.find({'bolsista': True}):
    print(aluno)

print("\nBuscando alunos não bolsistas:")
for aluno in alunos.find({'bolsista': False}):
    print(aluno)




# Atualizando documentos
alunos.update_many({}, {'$set': {'mensalidade': 0}})
alunos.update_many({'bolsista': True}, {'$set': {'desconto': 0}})

# Concedendo descontos com base na nota dos bolsistas
alunos.update_many({'bolsista': True, 'nota': {'$gt': 9}}, {'$set': {'desconto': 100}})
alunos.update_many({'bolsista': True, 'nota': {'$gte': 7, '$lte': 9}}, {'$set': {'desconto': 50}})

# Insere o atributo 'cidade' nos alunos
alunos.update_many({}, {'$set': {'cidade': ''}})

# Removendo documentos
alunos.delete_one({'_id': ObjectId('5af58b15c369ce419987ca03')})





# Pesquisa Textual
alunos.create_index([('nome', 'text'), ('bolsista', 'text'), ('nota', 'text'), ('cidade', 'text')])
print("\nPesquisando alunos por texto:")
print(alunos.find({'$text': {'$search': 'Paulo Rio de Janeiro'}}))


# Agregação
pipeline = [
    {'$match': {'bolsista': True}},
    {'$group': {'_id': '$bolsista', 'total': {'$sum': '$mensalidade'}}}
]

result = list(alunos.aggregate(pipeline))
print("\nTotal de mensalidades dos bolsistas:")
print(result)







# Fechando a conexão com o MongoDB
client.close()
