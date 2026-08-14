//selecionar o container principal 
const container = document.getElementById("container")//acessar

// 1 appendchild - adiciona no final 
document.getElementById("btnAppend").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Parágrafo adicionado com appendchild no final";
    container.appendChild(p);
});

// 2 prepend - adiciona no inicio 
document.getElementById("btnPrepend").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = ("Parágrafo adicionado com  prepend no inicio");
    container.prepend(p);
});

// 3 insertBefore - insere antes do primero 
document.getElementById("btnInsertBefore").addEventListener("click", () => {
    const p = document.createElement("P");
    p.textContent = "Parágrafo inserido antes do primeiro";
    const primeiro = container.firstElementChild
    container.insertBefore(p, primeiro);
});

// 4 btnReplace - substitui no primiero parágrafo 
document.getElementById("btnReplace").addEventListener("click", () => {
const novo = document.createElement("p");
novo.textContent = "Primeiro parágrafo substituido"
const primeiro = container.firstElementChild;
primeiro.replaceWith(novo)
});

// 5 btnCard - criar card com botão de remover 
document.getElementById("btnCard").addEventListener("click", () => {
    const card = document.createElement("div");
    card.className = "card";

    const titulo = document.createElement("h3");
    titulo.textContent = "card Dinamico";

    const btnRemover = document.createElement("button");
    btnRemover.textContent = "remover";
    btnRemover.addEventListener("click", () => {
      container.removeChild(card);
    });

    card.appendChild(titulo);
    card.appendChild(btnRemover);
    container.appendChild(card);
});

// 6 manipilação de texto com textContent
document.getElementById("btnTextContent").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Texto em negrito usando text content";
    container.appendChild(p);
});


// 6 manipilação de texto com innerHTML
document.getElementById("btnInnerHTML").addEventListener("click", () => {
    const p = document.createElement("p");
    p.innerHTML = "<strong>Texto em negrito</strong> usando innerHTML";
    container.appendChild(p);
});

