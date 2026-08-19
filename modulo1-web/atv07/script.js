const botao = document.getElementById("buscar");
const resultado = document.getElementById("resultado");

botao.addEventListener("click", async () => {
    const cep = document.getElementById("cep").value.trim();

    if (cep === "") {
        resultado.innerHTML = "<p>Digite um CEP.</p>";
        return;
    }

    try {
        const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        const dados = await resposta.json();

        // Verifica se o CEP não foi localizado
        if (dados.erro) {
            resultado.innerHTML = "<p>CEP inválido ou não localizado.</p>";
            return;
        }

        // Exibe os dados encontrados
        resultado.innerHTML = `
            <h2>Endereço encontrado</h2>
            <p><strong>Logradouro:</strong> ${dados.logradouro}</p>
            <p><strong>Bairro:</strong> ${dados.bairro}</p>
            <p><strong>Cidade:</strong> ${dados.localidade}</p>
            <p><strong>UF:</strong> ${dados.uf}</p>
        `;
    } catch (erro) {
        resultado.innerHTML = `
            <p>Não foi possível realizar a consulta.</p>
        `;
    }
});