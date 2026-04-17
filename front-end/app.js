const URL_CALCULAR = "http://127.0.0.1:8000/calcular";
const URL_HISTORICO = "http://127.0.0.1:8000/historico";


function calcularCashback(c) {
    let valor = Number(c.valor_consulta);

    let cashbackBase = valor * 0.05;
    let cashbackVIP = 0;

    if (Number(c.id_tipo_cliente) === 1) {
        cashbackVIP = cashbackBase * 0.10;
    }

    let cashbackTotal = cashbackBase + cashbackVIP;

    if (valor > 500) {
        cashbackTotal *= 2;
    }

    return cashbackTotal;
}

function fazerRequisicao() {
    let request = new XMLHttpRequest();

    request.open("GET", URL_HISTORICO, true);

    request.onload = function () {
        if (this.status === 200) {
            let data = JSON.parse(this.responseText);
            exibirDados(data);
        } else {
            console.log("Erro na requisição do histórico");
        }
    };

    request.send();
}

function exibirDados(lista) {
    let tbody = document.getElementById("history-body");

    if (!tbody) return;

    tbody.innerHTML = "";

    lista.forEach(item => {
        let cashback = calcularCashback(item);

        tbody.innerHTML += `
            <tr class="text-center">
                <td class="px-6 py-4">${item.id_tipo_cliente}</td>
                <td class="px-6 py-4">R$ ${Number(item.valor_consulta).toFixed(2)}</td>
                <td class="px-6 py-4">${item.data_acesso || "-"}</td>
                <td class="px-6 py-4 text-[#00d1b2] font-bold">
                    R$ ${Number(cashback).toFixed(2)}
                </td>
            </tr>
        `;
    });
}

function enviarCalculo(tipo, valor) {
    let request = new XMLHttpRequest();

    request.open("POST", URL_CALCULAR, true);
    request.setRequestHeader("Content-Type", "application/json");

    request.onload = function () {
        if (this.status === 200) {
            console.log("Cashback calculado com sucesso!");
            fazerRequisicao(); 
        } else {
            console.log("Erro ao calcular cashback");
        }
    };

    let body = JSON.stringify({
        id_tipo_cliente: Number(tipo),
        valor_consulta: Number(valor)
    });

    request.send(body);
}

document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("btn_form");

    if (btn) {
        btn.addEventListener("click", function (e) {
            e.preventDefault();

            const tipo = document.getElementById("client-type").value;
            const valor = document.getElementById("purchase-value").value;

            if (!tipo || !valor) {
                console.log("Preencha todos os campos");
                return;
            }

            enviarCalculo(tipo, valor);
        });
    }

    const refresh = document.getElementById("refresh-history");

    if (refresh) {
        refresh.addEventListener("click", function () {
            fazerRequisicao();
        });
    }
    fazerRequisicao();
});