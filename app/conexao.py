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
        conn = pg.connect(
            database='postgres',
            user='postgres.kegawbegcqwwrczfrrcl',
            password='dskjfsdknfsjkdfhsdjkf',
            host='aws-1-us-east-2.pooler.supabase.com',
            port=6543,
            sslmode='require',
        )
        return conn

    except Exception as e:
        print("Erro ao conectar:", e)
        return None


def encerra_conexao(connect):
    if connect:
        connect.close()
        print("Conexão encerrada")
