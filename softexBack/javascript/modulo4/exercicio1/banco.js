import readlineSync from "readline-sync";
const rl = readlineSync;

function Banco(conta, saldo, tipoConta, agencia) {
    this.conta = conta;
    this.saldo = saldo;
    this.tipoConta = tipoConta;
    this.agencia = agencia;

    this.saldoAtual = function() {
        return this.saldo;
    }

    this.deposito = function(a) {
        this.saldo += a
    }

    this.saque = function(a) {
        this.saldo -= a
    }

    this.numConta = function(){
        return this.conta;       
    }

}

var bancoInter = new Banco (undefined, undefined, undefined, undefined)

bancoInter.conta = rl.question("Digite o numero da sua conta: ")
bancoInter.saldo = rl.questionFloat("Digite o valor do seu saldo: ")
bancoInter.tipoConta = rl.question("Digite o tipo da sua conta: ")
bancoInter.agencia = rl.question("Digite o numero da sua agencia: ")

console.log("\nNumero da conta: "+ bancoInter.numConta())
console.log("Tipo da conta: "+ bancoInter.tipoConta)
console.log("Agencia: "+ bancoInter.agencia)
console.log("Saldo: "+ bancoInter.saldo)
bancoInter.deposito(2000)
console.log("Saldo apos deposito de BRL2000: "+ bancoInter.saldoAtual())
bancoInter.saque(1200)
console.log("Saldo apos saque de BRL1200: "+ bancoInter.saldoAtual())