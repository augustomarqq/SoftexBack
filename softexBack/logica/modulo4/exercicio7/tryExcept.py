"""Atividade 7 - Try Except Adivinha Idade"""

while True:            
    
    try:
        nome = input("Digite o seu nome completo: ")
        if any (l.isdigit() for l in nome):
            raise Exception("Nome inválido, por favor preencha novamente")
        
        anoNasc = int(input("Em qual ano você nasceu? "))
        if anoNasc != int and not anoNasc >= 1922 and anoNasc <= 2021:
            raise Exception ("Data de nascimento inválida, por favor preencha novamente")
        
        idade = 2022 - anoNasc         
        print(f"O usuário {nome} vai completar {idade} anos em 2022")
        break
     
    except Exception as error:
        print(error)