"""Exercício 1"""

nome = input("Digite o nome do aluno: ")
faltas = int(input("Digite o número de faltas do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7 and faltas <= 3:
    print(f"O aluno {nome} tem média {media}, possui {faltas} faltas e está APROVADO!")
else:
    print(f"O aluno {nome} tem média {media}, possui {faltas} faltas e está REPROVADO!")
