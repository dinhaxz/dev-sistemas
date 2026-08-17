const botaoBuscar = document.getElementById("buscar");

botaoBuscar.addEventListener("click", () => {
    const nome = document.getElementById("usuario").value.trim();
    const perfil = document.getElementById("perfil");

    if (nome === "") {
        perfil.innerHTML = "Digite um usuário!";
        return;
    }

    fetch(`https://api.github.com/users/${nome}`)
        .then(resp => {
            if (!resp.ok) {
                throw new Error("Usuário não encontrado!");
            }

            return resp.json();
        })
        .then(usuario => {
            perfil.innerHTML = `
                <img src="${usuario.avatar_url}" 
                     alt="Foto de ${usuario.name || usuario.login}"
                     width="150">

                <h3>${usuario.name || "Nome não informado"}</h3>

                <p>${usuario.bio || "Biografia não informada."}</p>
            `;
        })
        .catch(() => {
            perfil.innerHTML = "Usuário não encontrado!";
        });
});