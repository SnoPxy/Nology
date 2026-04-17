
from app.conexao import connect, encerra_conexao
import psycopg2.extras

class cashbackModel:
    
    def __init__(self):
        self.conn = connect()
    
    def get_by_id(self, tipo_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                SELECT *
                FROM cashback
                WHERE id = %s;
            """, (tipo_id,))
            return cur.fetchone()

    def close(self):
        self.conn.close()

