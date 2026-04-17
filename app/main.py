import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.controller import consultaController
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from app.controller.cashbackController import CashbackController
from app.controller.consultaController import ConsultaController
from app.controller.tipoClienteController import TipoClienteController


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

controllerCashback = CashbackController()
controllerConsulta = ConsultaController()
controllerTipoCliente = TipoClienteController()


@app.post("/calcular")
async def calcular(request: Request):
    try:
        body = await request.json()
    except:
        body = await request.form()

    tipo_id = int(body.get("id_tipo_cliente"))
    valor = float(body.get("valor_consulta"))

    resultado = controllerCashback.calculate_cashback(tipo_id, valor)

    if not resultado:
        return JSONResponse(
            status_code=404,
            content={"erro": "Tipo de cliente não encontrado"}
        )

    ip = request.client.host

    controllerConsulta.save_consult(
        ip=ip,
        data_acesso=datetime.datetime.now(),
        tipo_id=tipo_id,
        id_cashback=resultado["id_cashback"],
        valor=valor,
    )

    return JSONResponse(content=resultado)


@app.get("/historico")
def historico(request: Request):
    ip = request.client.host

    dados = controllerConsulta.consult_ip(ip)
    lista = []

    for dado in dados:

        cashback = controllerCashback.get_cashback_by_id(dado["id_cashback"])
        tipo_cliente = controllerTipoCliente.get_id(dado["id_tipo_cliente"])

        consulta = {"ip_usuario": dado['ip'], "data_acesso": dado['data_acesso'], "valor_consulta": dado['valor'], "id_tipo_cliente": tipo_cliente['id'],
                    "nome_tipo_cliente": tipo_cliente['nome'], "id_cashback": cashback["id"], "valor_cashback": cashback["valor"]}

        lista.append(consulta)

    return JSONResponse(content=jsonable_encoder(lista))
