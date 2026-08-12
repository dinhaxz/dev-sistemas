// 1. Informações do jogador
const nomeJogador = "Carlos";
let idade = 20;
let online = true;

// Objeto com o jogo favorito
const jogoFavorito = {
    nome: "Minecraft",
    anoLancamento: 2011
};

// Array com as últimas 3 pontuações
const pontuacoes = [850, 920, 780];

// 2. Mostrar os valores e seus tipos
console.log("Nome:", nomeJogador, "| Tipo:", typeof nomeJogador);
console.log("Idade:", idade, "| Tipo:", typeof idade);
console.log("Online:", online, "| Tipo:", typeof online);
console.log("Jogo favorito:", jogoFavorito, "| Tipo:", typeof jogoFavorito);
console.log("Pontuações:", pontuacoes, "| Tipo:", typeof pontuacoes);

// 3. Alterar idade e status online
idade = 21;
online = false;

console.log("Nova idade:", idade);
console.log("Novo status online:", online);

// A linha abaixo causaria erro, pois nomeJogador é uma constante:
// nomeJogador = "João";

// 4. Desafio extra: calcular a média
const media = (pontuacoes[0] + pontuacoes[1] + pontuacoes[2]) / 3;

console.log(`A média de pontos do jogador ${nomeJogador} foi: ${media}`);