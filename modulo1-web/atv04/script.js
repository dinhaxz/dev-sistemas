const tituloInput = document.getElementById("tituloCard");
const botaoCriar = document.getElementById("criarCard");
const cardsContainer = document.getElementById("cardsContainer");

botaoCriar.addEventListener("click", function () {
    const titulo = tituloInput.value.trim();

    if (titulo === "") {
        alert("Digite um título para o card.");
        return;
    }

    // Cria o card
    const card = document.createElement("div");

    // Cria o título
    const h3 = document.createElement("h3");
    h3.textContent = titulo;

    // Cria o botão Remover
    const botaoRemover = document.createElement("button");
    botaoRemover.textContent = "Remover";

    // Remove o card ao clicar no botão
    botaoRemover.addEventListener("click", function () {
        card.remove();
    });

    // Adiciona os elementos ao card
    card.appendChild(h3);
    card.appendChild(botaoRemover);

    // Adiciona o card ao container
    cardsContainer.appendChild(card);

    // Limpa o input
    tituloInput.value = "";
    tituloInput.focus();
});