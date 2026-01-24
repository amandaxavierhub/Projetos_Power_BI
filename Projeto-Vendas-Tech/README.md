# Power BI| Análise de Vendas | KPIs


1. [Introdução](#introdução)
2. [Principais Indicadores](#principais-indicadores)
3. [Ferramentas Utilizadas](#ferramentas-utilizadas)
4. [Códigos](#códigos)
5. [Arquivos](#arquivos)
6. [Links](#links)


## Introdução

Dashaboard| Vendas e Performance Comercial

Este projeto foi desenvolvido para análise de vendas de uma empresa do setor de tecnologia. Os dados utilizados são fictícios e foram desenvolvidos apenas para aplicação do conteúdo.

## Principais Indicadores
### O relatório permite acompanhar os principais indicadores:
* Receita Total.
* Quantidade total vendida.
* Ticket Médio.
* Produto Líder de vendas (QTD).
* Produto Líder de Vendas (Receita).
* Top 10 produtos por faturamento.
* Detalhe de vendas por Loja.
* Distribuição por Categoria.
* KPI informátivo.

## Ferramentas Utilizadas

- Python| pandas
- SqLiteStudio
- Power BI
- Canva (apresentação do portfólio)

## Códigos
Foi utilizada a biblioteca pandas para gerar a base de vendas em formato db.

~~~~Python
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


Produtos = (
    [(101,"Celular","Eletrônicos",2500)] * 6 +
    [(102,"Notebook","Eletrônicos",4500)] * 3 +
    [(103,"Fone Bluetooth","Eletrônicos",300)] * 7 +
    [(104,"Carregador","Acessórios",120)] * 9 +
    [(105,"Capa de Celular","Acessórios",80)] * 15 +
    [(106,"Mouse","Acessórios",150)] * 3 +
    [(107,"Teclado","Acessórios",220)] * 2 +
    [(108,"TV","Eletrônicos",3800)] * 2 +
    [(109,"Smartwatch","Eletrônicos",900)] * 4 +
    [(110,"Caixa de Som","Eletrônicos",600)] * 3 +
    [(111,"Mochila","Utilidades",200)] * 2 +
    [(112,"Garrafa Térmica","Utilidades",150)] * 2 +
    [(113,"Fone com Fio","Acessórios",90)] * 4 +
    [(114,"Hub USB","Acessórios",180)] * 3 +
    [(115,"Suporte Celular","Utilidades",70)] * 2
)


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

df.to_csv("base_vendas.csv", index=False)

#carregar o arquivo
df =    pd.read_csv("base_vendas.csv")


#Conectar ao banco

conn = sqlite3.connect("base_vendas.db")

#salva no banco

df.to_sql("base_vendas", conn, if_exists="replace", index=False)

conn.close()

~~~~

## Arquivos
Arquivos
📄 Relatório em PDF:
- [Visualizar código](./base_de_vendas.py)
- [Visualizar relatório](./porfolio_base_de_vendas.pdf)

## Links

[![YouTube Channel](https://img.shields.io/badge/YouTube-Análise%20em%20Choque-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@analiseemchoque) 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]([https://www.linkedin.com/in/amandaxaviers])
