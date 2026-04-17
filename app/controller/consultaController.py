from app.model.modelConsulta import consultaModel


class ConsultaController:

    def __init__(self):
        self.model = consultaModel()

    def save_consult(self, ip, data_acesso, tipo_id, id_cashback, valor):
        self.model.insert_consult_BD(
            ip, data_acesso, tipo_id, id_cashback, valor)

    def consult_ip(self, ip):
        return self.model.consult_ip(ip)

    def close_connection(self):
        self.model.close()
