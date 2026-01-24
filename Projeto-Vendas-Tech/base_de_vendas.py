import pandas as pd
import random
from datetime import datetime, timedelta
import sqlite3


# Vendedores


Vendedores = [ 
    (1,"Ana Julia"), (2,"Bruno Costa"), (3,"Carlos Lima"),
    (4,"Daniela Rocha"), (5,"Eduardo Alves"),
    (6,"Fernanda Pires"), (7,"Gabriel Santos"), (8,"Helena Souza"),
    (9,"Igor Martins"), (10,"Juliana Mendes"),
    (11,"Lucas Teixeira"), (12,"Marina Lopes"),
    (13,"Nathan Ribeiro"), (14,"Paula Nogueira"), (15,"Rafael Nunes")
]

#Loja Por Vendedor (5 por loja)

lojas = {
     1:"Loja 1",2:"Loja 1",3:"Loja 1",4:"Loja 1",5:"Loja 1",
    6:"Loja 2",7:"Loja 2",8:"Loja 2",9:"Loja 2",10:"Loja 2",
    11:"Loja 3",12:"Loja 3",13:"Loja 3",14:"Loja 3",15:"Loja 3"
}


#Produtos


Produtos = [
     (101,"Celular","Eletrônicos",2500),
    (102,"Notebook","Eletrônicos",4500),
    (103,"Fone Bluetooth","Eletrônicos",300),
    (104,"Carregador","Acessórios",120),
    (105,"Capa de Celular","Acessórios",80),
    (106,"Mouse","Acessórios",150),
    (107,"Teclado","Acessórios",220),
    (108,"TV","Eletrônicos",3800),
    (109,"Smartwatch","Eletrônicos",900),
    (110,"Caixa de Som","Eletrônicos",600),
    (111,"Mochila","Utilidades",200),
    (112,"Garrafa Térmica","Utilidades",150),
    (113,"Fone com Fio","Acessórios",90),
    (114,"Hub USB","Acessórios",180),
    (115,"Suporte Celular","Utilidades",70)
]


#Datas

data_inicio = datetime(2024,3,1)
datas = [(data_inicio  + timedelta (days=i)) for i in range(31)]

#Geração de Base

dados = []


for _ in range(10000):
    vendedor = random.choice(Vendedores)
    produto = random.choice(Produtos)
    data = random.choice(datas)


#Quantidade com viés

    if produto[3] > 2000:
        quantidade = random.randint(1,2)
    elif produto[3] > 500:
        quantidade = random.randint(1,3)
    else:
        quantidade = random.randint(1,5)


    dados.append([
        vendedor[0],
        vendedor[1],
        produto[0],
        produto[1],
        produto[2],
        quantidade,
        produto[3],
        data.strftime("%y-%m-%d"),
        lojas[vendedor[0]]
    ])


#DataFrame


df = pd.DataFrame(dados, columns=[
    "id_vendedor", "nome_vendedor",
    "id_produto", "nome_produto", "categoria_produto",
    "quantidade", "valor_unitario", "data_venda", "loja"
])

#Exporta

df.to_csv("base_vendas_2024.csv", index=False)

#carregar o arquivo
df =    pd.read_csv("base_de_vendas_2024.csv")


#Conectar ao banco

conn = sqlite3.connect("base_de_vendas_2024.db")

#salva no banco

df.to_sql("base_de_vendas_2024", conn, if_exists="replace", index=False)

conn.close()

print("Banco criado com sucesso")

print("Base criada com sucesso", df.shape)
