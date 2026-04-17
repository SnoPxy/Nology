const URL_CALCULAR = "https://testeapp-d378.onrender.com/calcular";
const URL_HISTORICO = "https://testeapp-d378.onrender.com/historico";

async function post(event) {
    event.preventDefault();

    let request = new XMLHttpRequest();
    request.open("POST", URL_CASHBACK, true);
    request.setRequestHeader("Content-type", "application/json");

    let id = document.getElementById("client-type").value;
    let valor = document.getElementById("purchase-value").value;

    let body = {
        "tipo_id": id,
        "valor": valor,
    };

    request.onload = function () {
        console.log(this.responseText);
    };

    request.send(JSON.stringify(body));
}

function fazerrequisicao() {
    fetch(URL_HISTORICO)
        .then(response => response.json())
        .then(cenouras => {
            console.log(cenouras);

            const div = document.getElementById("history-body");

            div.innerHTML = "";

            cenouras.forEach(cenoura => {
                div.innerHTML += `
                    <tr>
                        <td class="px-6 py-4 text-center">${cenoura.nome_tipo_cliente}</td>
                        <td class="px-6 py-4 text-center">R$${Number(cenoura.valor_consulta).toFixed(2)}</td>
                        <td class="px-6 py-4 text-center">
                            ${new Date(cenoura.data_acesso).toLocaleDateString('pt-BR')}
                        </td>
                        <td class="px-6 py-4 text-center ${cenoura.valor_consulta > 500 ? 'text-[#00d1b2]' : ''}">
                            R$${calcularCashback(cenoura).toFixed(2)}
                        </td>
                    </tr>
                `;
            });
        })
        .catch(error => {
            console.log("Erro:", error);
        });
}

function calcularCashback(cenoura) {
    let valor = Number(cenoura.valor_consulta);
    let tipo = Number(cenoura.id_tipo_cliente);

    let cashbackBase = valor * 0.05;
    let cashbackTotal = cashbackBase;

    // VIP (id = 1) ganha +10% sobre o cashback base
    if (tipo === 1) {
        cashbackTotal += cashbackBase * 0.10;
    }

    // promoção: dobra acima de 500
    if (valor > 500) {
        cashbackTotal *= 2;
    }

    return cashbackTotal;
}

document.getElementById("btn_form").addEventListener("click", (e) => {
    post(e);

    setTimeout(() => {
        fazerrequisicao();
    }, 1000);
});
