import psycopg2.extras
from app.conexao import connect, encerra_conexao


class tipoClienteModel:

    def __init__(self):
        self.conn = connect()

    def get_id(self, tipo_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                SELECT id, nome
                FROM tipo_cliente
                WHERE id = %s;
            """, (tipo_id,))
            return cur.fetchone()

    def close(self):
        self.conn.close()
