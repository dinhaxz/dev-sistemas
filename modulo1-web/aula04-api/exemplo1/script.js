document.addEventListener("DOMContentLoaded", function () {
  const duploClique = document.getElementById("duploClique");
  duploClique.addEventListener("dblclick", () => {
    alert("Você deu um duplo click nesse parágrafo");
    console.log("this se refere a:", this); // exibe o elemento clicado
  });

// demonstração arrow function x função regular
  duploClique.addEventListener("click", () => {
    console.log("Arrow funtion this: ", this);
  });
// 2. remoção de elemetos
  const btnRemoveritem2 = document.getElementById("btnRemoverItem2");
  const lista = document.getElementById("lista");

  btnRemoveritem2.addEventListener("click", function () {
    const item2 = document.getElementById("item2");
    if (item2) {
      item2.remove();
    }
  });

// remoção com thid.removeChild() para item 3
  const item3 = document.getElementById("item3");
  if (item3) {
    lista.removeChild(item3); // metodo mais antigo
    console.log("Iten 3 remocido usando removeChild()");
  }

// 3. delegação de eventos
const tarefas = document.getElementById("tarefas");
const btnAdicionarTarerfa = document.getElementById("btnAdicionarTarefa");
let contador = 4;

// adionar novas tarefas dinamicamente 
btnAdicionarTarerfa.addEventListener("click", function() {
    const li = document.createElement("li");
    li.textContent = "Tarefa" + contador;
    contador++;
    tarefas.appendChild(li); 
});

// delegação: remover tarefas ao clicar 
tarefas.addEventListener("click", function () {
    if(event.target.tagName === "LI") {
        event.target.remove();
        console,log("Tarefa removida: ", event.target.textContent);
    }
});
});
