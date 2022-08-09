import readlineSync from "readline-sync";
var rl = readlineSync;

var n1 = rl.questionFloat("Primeira nota: ");
var n2 = rl.questionFloat("Segunda nota: ");
var n3 = rl.questionFloat("Terceira nota: ");

var media = (n1 + n2 + n3) / 3;

if (media >= 7) {
    console.log("Sua média é "+ media.toFixed(2) +" e você está APROVADO!");
} else
    console.log("Sua média é "+ media.toFixed(2) + " e você está REPROVADO!");