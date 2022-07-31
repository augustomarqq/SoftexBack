"""Exercício 2 - Melhor Habilitação"""

rodas = int(input("Quantas rodas têm no veículo que você dirige? "))
peso = float(input("Qual o peso do veículo que você dirige? "))
passag = int(input("Quantos passageiros cabem no veículo que você dirige? "))

if rodas > 1 and rodas < 4:
    print("A melhor categoria de habilitação para o veículo informado é a CATEGORIA A")
elif rodas == 4 and passag <= 8 and peso <= 3500:
    print("A melhor categoria de habilitação para o veículo informado é a CATEGORIA B")
elif rodas >= 4 and peso > 3500 and peso < 6500:
    print ("A melhor categoria de habilitação para o veículo informado é a Categoria C")
elif rodas >= 4 and passag > 8:
    print ("A melhor categoria de habilitação para o veículo informado é a Categoria D")
elif rodas >= 4 and peso > 6000:
    print ("A melhor categoria de habilitação para o veículo informado é a Categoria E")
else:
    print("Não há habilitação ideal para os dados inseridos")
