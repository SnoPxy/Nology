import psycopg2 as pg
from psycopg2 import Error
import psycopg2.extras
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def connect():
    try:
        psw = os.getenv("DB_PASSWORD")
        connect = pg.connect(
            database = 'nology',
            user = 'postgres',
            password = psw,
            host = '127.0.0.1',
            port = '5432',
        )
        
        return connect

    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        

def encerra_conexao(connect):
    if connect:
        connect.close()
        print("Conexão encerrada")