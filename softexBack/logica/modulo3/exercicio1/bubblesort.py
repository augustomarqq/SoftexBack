import random

def bubble_sort(lista):
    
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                #troca de elementos nas posições i e i+1
                lista[i], lista [i+1] = lista[i+1], lista [i]


any_numbers = random.sample(range(1, 100), 10)

lista = any_numbers
print("\nLista randomizada:")
print(lista)
bubble_sort(lista)
print("\nLista ordenada utilizando o Buuble Sort:")
print(lista)