from app.conexao import connect, encerra_conexao
import socket
import psycopg2.extras

class consultaModel:
    
    def __init__(self):
        self.conn = connect()
        self.hostname = socket.gethostname()
        self.ip_local = socket.gethostbyname(self.hostname)
        
        
    def insert_consult_BD(self,ip, data_acesso, tipo_id, id_cashback, valor):
      with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                INSERT INTO consultas (ip, data_acesso, id_tipo_cliente, id_cashback,valor)
                VALUES (%s, %s, %s, %s, %s);
            """, (ip, data_acesso, tipo_id, id_cashback, valor))
            self.conn.commit()
            
    def consult_ip(self, ip):
         with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                SELECT *
                FROM consultas
                WHERE ip = %s
                ORDER BY data_acesso DESC;
            """, (ip,))
            return cur.fetchall()
        
        
