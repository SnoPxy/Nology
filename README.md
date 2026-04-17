#  Analise de Cashback

Projeto full stack desenvolvido com **frontend em JavaScript (HTML/CSS)** e **backend em Python utilizando FastAPI**, seguindo arquitetura **MVC** e princípios de **POO (Programação Orientada a Objetos)**.

---

##  Resumo

O sistema realiza o cálculo de cashback baseado no tipo de cliente e no valor da compra. A aplicação consome uma API construída em FastAPI e exibe os resultados em uma interface web dinâmica.

---

## Linguagens Utilizadas

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)      
* TailwindCSS

### Backend

* Python 3
* FastAPI
* Uvicorn

---

## 🧠 Arquitetura do Projeto

O backend foi estruturado utilizando o padrão MVC:

**POO** -> Programação orientada a objeto
* **Model** → Responsável pelo acesso e manipulação dos dados
* **Controller** → Regras de negócio e lógica da aplicação
* **View** → Consumo da API pelo frontend (JavaScript)
* 

---

## 📁 Estrutura do projeto

```

  app/
 │   ├── controller/
 │   │   ├── cashbackController.py
 │   │   ├── consultaController.py
 │   │   └── tipoClienteController.py
 │   ├── model/
 │   │   └── modelCashback.py
 │   └── main.py

frontend/
 ├── index.html
 ├── app.js
 ├── style.css
```

---

## Funcionalidades

* Cálculo de cashback por tipo de cliente
* Aplicação de regras de negócio:

  * Cashback base por percentual
  * Bônus para clientes VIP
  * Multiplicador para compras acima de R$ 500
* Exibição dinâmica dos resultados na interface

---

## Regra de negócio do cashback

* Cashback base: percentual do valor da compra
* Cliente VIP: recebe bônus adicional
* Compras acima de R$ 500: cashback dobrado


## Exemplo de requisição API

```http
GET /cashback/{tipo_id}/{valor_compra}
```

### Resposta:

```json
{
  "tipo_cliente": "VIP",
  "valor_compra": 600,
  "cashback": 120.0
  "..."
}
```
## Autor

Desenvolvido por Arthur Lopes
