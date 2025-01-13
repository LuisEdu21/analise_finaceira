import psycopg2 as pg
import os 
from dotenv import load_dotenv

load_dotenv()

def conectar_com_banco():

    conexao = pg.connect(host = os.getenv('host_DB'), 
                database=os.getenv('database_DB'),
                user=os.getenv('user_DB'), 
                password=os.getenv('pass_DB'))
  
    return conexao

def suspender_conexao(conn,cursor):

    cursor.close()
    conn.close()

    return

def criar_tabelas():

    conexao = conectar_com_banco()

    sql = [
        "CREATE SCHEMA financeiro AUTHORIZATION postgres;",
        "CREATE TABLE financeiro.acoes (id SERIAL PRIMARY KEY, simbolo VARCHAR(10) NOT NULL, nome VARCHAR(100),preco_atual DECIMAL(10, 2),variacao_percentual DECIMAL(5, 2),dividendos_por_acao DECIMAL(10, 2),volume BIGINT,data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);",
        "CREATE TABLE financeiro.metas_investimentos (id SERIAL PRIMARY KEY,nome_meta VARCHAR(100),quantidade_desejada INT,quantidade_atual INT DEFAULT 0,valor_meta DECIMAL(15, 2),valor_investido DECIMAL(15, 2),progresso DECIMAL(5, 2),data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);",
        "CREATE TABLE financeiro.historico_investimentos (id SERIAL PRIMARY KEY,mes VARCHAR(10),ano INT,saldo_inicial DECIMAL(15, 2),valor_investido DECIMAL(15, 2),valor_retirado DECIMAL(15, 2),dividendos_recebidos DECIMAL(15, 2),valorizacao_carteira DECIMAL(15, 2),carteira_total DECIMAL(15, 2));",
        "CREATE TABLE financeiro.gastos (id SERIAL PRIMARY KEY,descricao VARCHAR(255),categoria VARCHAR(50),valor DECIMAL(10, 2),data DATE,metodo_pagamento VARCHAR(50),parcela INT DEFAULT 1,total_parcelas INT DEFAULT 1,responsavel VARCHAR(100));",
        "CREATE TABLE financeiro.metas_gastos (id SERIAL PRIMARY KEY,nome_meta VARCHAR(100),limite_valor DECIMAL(15, 2),mes VARCHAR(10),ano INT,valor_gasto DECIMAL(15, 2) DEFAULT 0,status VARCHAR(20) DEFAULT 'Em Progresso');",
        "CREATE TABLE financeiro.lista_compras (id SERIAL PRIMARY KEY,nome_item VARCHAR(255),prioridade INT,valor_estimado DECIMAL(10, 2),status VARCHAR(20) DEFAULT 'Pendente',data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);",
        "CREATE TABLE financeiro.compras_realizadas (id SERIAL PRIMARY KEY,nome_item VARCHAR(255),valor DECIMAL(10, 2),data DATE,foi_autorizado BOOLEAN DEFAULT FALSE);"
    ]

    cursor = conexao.cursor()

    with open("config/configuracoes.txt", "r") as arquivo:
        resultado = arquivo.read()

    if resultado == 'N':
        for consulta in sql:
            cursor.execute(consulta)
            conexao.commit()

        with open("config/Tabela.txt", "w") as arquivo:
            arquivo.write("S")

    else:
        print('Tabela ja existe')

    suspender_conexao(conexao,cursor)

    return print('Finalizado o processo de criacao do banco')