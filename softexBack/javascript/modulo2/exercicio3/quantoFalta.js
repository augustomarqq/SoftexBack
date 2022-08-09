import readlineSync from "readline-sync";
var rl = readlineSync;

var n1 = rl.questionFloat("Primeira nota: ");
var n2 = rl.questionFloat("Segunda nota: ");

var proxNota = 21 - (n1 + n2)

if (proxNota <= 10)
    console.log("A nota mínima necessária na Terceira Prova para ser APROVADO com Média 7 é: "+ proxNota.toFixed(2))
else
    console.log("Mesmo tirando 10 na Terceira Prova não há como passar por média, portanto você está REPROVADO!")