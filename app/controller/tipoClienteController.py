from app.model import modelTipoCliente


class TipoClienteController:

    def __init__(self):
        self.model = modelTipoCliente.tipoClienteModel()

    def get_id(self,  tipo_id):
        return self.model.get_id(tipo_id)

    def closer_connection(self):
        self.model.close()
