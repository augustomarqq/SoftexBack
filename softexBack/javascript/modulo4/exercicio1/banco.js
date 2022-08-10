function Banco(conta, saldo, tipoConta, agencia) {
    this.conta = conta;
    this.saldo = saldo;
    this.tipoConta = tipoConta;
    this.agencia = agencia;

    this.saldoAtual = function() {
        return this.saldo = saldo;
    }

    this.deposito = function(a) {
        saldo += a
    }

    this.saque = function(a) {
        saldo -= a
    }

    this.numConta = function(){
        return this.conta = conta;       
    }

}

var bancoInter = new Banco ("829747-9", 10000, "corrente", "001")

console.log("Numero da conta: "+ bancoInter.numConta())
console.log("Tipo da conta: "+ bancoInter.tipoConta)
console.log("Agencia: "+ bancoInter.agencia)
console.log("Saldo: "+ bancoInter.saldo)
bancoInter.deposito(2000)
console.log("Saldo apos deposito de BRL2000: "+ bancoInter.saldoAtual())
bancoInter.saque(1200)
console.log("Saldo apos saque de BRL1200: "+ bancoInter.saldoAtual())