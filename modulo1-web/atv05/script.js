const caixas = document.querySelectorAll(".caixa");

const cores = [
    { nome: "amarelo", valor: "yellow" },
    { nome: "roxo", valor: "purple" },
    { nome: "laranja", valor: "orange" },
    { nome: "rosa", valor: "pink" },
    { nome: "azul-claro", valor: "deepskyblue" }
];

caixas.forEach(function (caixa) {
    caixa.addEventListener("dblclick", function () {
        console.log(this);

        const indiceAleatorio = Math.floor(Math.random() * cores.length);
        const novaCor = cores[indiceAleatorio];

        this.style.backgroundColor = novaCor.valor;

        alert("A nova cor da caixa é: " + novaCor.nome);
    });
});
