"""Atividade 6 - Adivinha Idade"""

while True:
    try:        
        nome = input("Digite o seu nome completo: ")
        anoNasc = int(input("Em qual ano você nasceu? "))
        idade = 2022 - anoNasc

        if anoNasc >= 1922 and anoNasc <= 2021:
            print (f"O usuário {nome} vai completar {idade} anos em 2022")
            break
        else:
            print("Dados inválidos, por favor preencha novamente")
    except:
        print("Dados inválidos, por favor preencha novamente")