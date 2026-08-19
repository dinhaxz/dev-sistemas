const cidade = document.getElementById("cidade");
const buscar = document.getElementById("buscar");
const resultado = document.getElementById("resultado");

buscar.addEventListener("click", () => {
    const [lat, lon] = cidade.value.split(",");

    const nomeCidade = cidade.options[cidade.selectedIndex].text;

    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    resultado.innerHTML = "Consultando clima...";

    fetch(url)
        .then(resposta => {
            if (!resposta.ok) {
                throw new Error("Erro na consulta");
            }

            return resposta.json();
        })
        .then(data => {
            const temperatura = data.current_weather.temperature;

            let corFundo;
            let icone;

            if (temperatura < 20) {
                corFundo = "linear-gradient(180deg, #2196f3, #0d47a1)";
                icone = "❄️";
            } else if (temperatura <= 30) {
                corFundo = "linear-gradient(180deg, #78909c, #455a64)";
                icone = "🌤️";
            } else {
                corFundo = "linear-gradient(180deg, #ff9800, #f44336)";
                icone = "☀️";
            }

            document.body.style.background = corFundo;

            resultado.innerHTML = `
                <h2>${nomeCidade}</h2>
                <div style="font-size: 60px;">${icone}</div>
                <p>Temperatura atual: <strong>${temperatura} °C</strong></p>
            `;
        })
        .catch(erro => {
            resultado.innerHTML = `
                <p>Não foi possível consultar os dados do clima.</p>
            `;

            console.error(erro);
        });
});