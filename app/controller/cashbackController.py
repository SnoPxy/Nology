from app.model import modelCashback


class CashbackController:
    def __init__(self):
        self.model = modelCashback.cashbackModel()

    def get_cashback_by_id(self, tipo_id):
        return self.model.get_by_id(tipo_id)

    def calculate_cashback(self, tipo_id, value_sale):
        tipo = self.model.get_by_id(tipo_id)

        if not tipo:
            return None

        a = tipo['valor']
        cashback = value_sale * (a/100)

        return {
            "tipo_cliente": tipo['id_cliente'],
            "valor_compra": value_sale,
            "cashback": cashback,
            "id_cashback": tipo['id']
        }

    def close_connection(self):
        self.model.close()
