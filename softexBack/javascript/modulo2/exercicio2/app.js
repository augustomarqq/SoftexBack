import { somar, subtrair , multiplicar , dividir } from "./funcoes.js";
import readlineSync from "readline-sync";
const rl = readlineSync;

var num1 = rl.questionFloat("Valor 1: ");
var num2 = rl.questionFloat("Valor 2: ");

while(true){

    var op = rl.question("Escolha a operacao a ser realizada:\n[+]\n[-]\n[*]\n[/]\n ");

    if (op == "+"){        
        somar(num1, num2);        
        break;        
    } else if (op == "-"){
        subtrair(num1, num2);
        break;
    } else if (op == "*"){
        multiplicar(num1, num2);
        break;
    } else if (op == "/"){
        dividir(num1, num2);
        break;
    } else
        console.log("Escolha uma operacao válida!\n");
}