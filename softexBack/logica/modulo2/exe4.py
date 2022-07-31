def calculadora (num1, num2, operacao):
          
    if operacao == 1:
        soma = num1 + num2
        return soma
    elif operacao == 2:
        subtracao = num1 - num2
        return subtracao
    elif operacao == 3:
        multiplicacao = num1 * num2
        return multiplicacao
    elif operacao == 4:
        divisao = num1 / num2
        return divisao
    else:
        return 0

op = int(input("Escolha o tipo de operação a ser utilizado sendo: \n [1] Soma; \n [2] Subtração; \n [3] Multiplicação; \n [4] Divisão: \n"))
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
print(f"O resultado foi {calculadora(n1, n2, op)}")