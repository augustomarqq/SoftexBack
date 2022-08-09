import readlineSync from "readline-sync";

var num1 = readlineSync.question("Digite o primeiro valor da operação: ");
var num2 = readlineSync.question("Digite o segundo valor da operação: ");
var res = parseFloat(num1) + parseFloat (num2);

console.log(num1+ "+" +num2+ "=" +res);
readlineSync.question("Aperte qualquer botão para sair");