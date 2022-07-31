import random

def insertion_sort(lista):
    
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave


any_numbers = random.sample(range(1, 100, 2), 30)

lista = any_numbers
print("\nLista randomizada:")
print(lista)
insertion_sort(lista)
print("\nLista ordenada utilizando o Insertion Sort:")
print(lista)