import readlineSync from "readline-sync";
const rl = readlineSync;

const somar = (a, b) => a + b

const subtrair = (a, b) => a - b

const multiplicar = (a, b) => a * b

const dividir = (a, b) => a / b

function printaResto(a, b) {    
    return console.log("O resultado da divisão entre "+ a +" e "+ b +" é = "+ (a / b).toFixed(2) +"\nE o resto é = "+ a%b)
}

export function calculadora() {

var n1 = rl.questionFloat("Valor 1: ");
var n2 = rl.questionFloat("Valor 2: ");

while(true) {
    
    var op = rl.question("Escolha a operacao a ser realizada:\n[+]\n[-]\n[*]\n[/]\n ");

    if (op == "+") {        
        console.log("O resultado da soma entre "+ n1 +" e "+ n2 +" é = "+ somar(n1, n2));
        break;       
    } else if (op == "-") {        
        console.log("O resultado da subtração entre "+ n1 +" e "+ n2 +" é = "+ subtrair(n1, n2));
        break;   
    } else if (op == "*") {        
        console.log("O resultado da multiplicação entre "+ n1 +" e "+ n2 +" é = "+ multiplicar(n1, n2));
        break;
    } else if (op == "/") {        
        if (n1%n2 == 0)
            console.log("O resultado da divisão entre "+ n1 +" e "+ n2 +" é = "+ dividir(n1, n2));
        else
            return printaResto(n1, n2);
            break;
    } else
        console.log("Escolha uma operação válida!\n");
};
};