from rich import print
import os

# Constantes
votosBolsonaro = 0
votosCiro = 0
votosLula = 0
branco = 0
nulo = 0

while True:
    # Tela de Apresentacao
    print('*'*40)
    print('VOTAÇÃO PARA PRESIDENTE DA REPÚBLICA')
    print('*'*40)
    
    # Votacao
    try:
        voto = int(input('Em quem você deseja votar para presidente? \n'))
        if voto == 13:
            votosLula += 1
        elif voto == 22:
            votosBolsonaro += 1
        elif voto == 12:
            votosCiro += 1
        elif voto == 0:
            branco += 1
        else:
            nulo += 1
        os.system('cls')
        try:
            finalizar = int(input('Deseja finalizar a votação? \n [1] SIM \n [2] NÃO \n' ))
            if finalizar == 1:
                os.system('cls')
                print('VOTAÇÃO FINALIZADA! \n')
                if votosBolsonaro > votosLula and votosBolsonaro > votosCiro:
                    print(f'O presidente eleito foi Bolsonaro com o total de {votosBolsonaro} votos \n')
                elif votosLula > votosBolsonaro and votosLula > votosCiro:
                    print(f'O presidente eleito foi Lula com o total de {votosLula} votos \n')
                elif votosCiro > votosLula and votosCiro > votosBolsonaro:
                    print(f'O presidente eleito foi Ciro com o total de {votosCiro} votos \n')
                elif votosCiro == votosLula and votosCiro > votosBolsonaro and votosLula > votosBolsonaro:
                    print('A votação será decidida no segundo turno entre Ciro e Lula! \n')
                elif votosBolsonaro == votosLula and votosBolsonaro > votosCiro and votosLula > votosCiro:
                    print('A votação será decidida no segundo turno entre Bolsonaro e Lula! \n')
                elif votosBolsonaro == votosCiro and votosBolsonaro > votosLula and votosCiro > votosLula:
                    print('A votação será decidida no segundo turno entre Bolsonaro e Ciro! \n')
                else:
                    pass
                print("NÚMERO TOTAL DE VOTOS: \n")
                print(f'[on green]Bolsonaro:[/] {votosBolsonaro}')
                print(f'[on blue]Ciro:[/] {votosCiro}')
                print(f'[on red]Lula:[/] {votosLula}')
                print(f'[on black]Nulos:[/] {nulo}')
                print(f'[on white]Branco:[/] {branco}')
                break
            elif finalizar == 2:
                os.system('cls')
                continue
            else:
                pass
        except:
                os.system('cls')
                print('Digite apenas 1 ou 2 \n')
                finalizar = int(input('Deseja finalizar a votação? \n [1] SIM \n [2] NÃO \n' ))
                if finalizar == 1:
                    os.system('cls')
                    print('VOTAÇÃO FINALIZADA! \n')
                    if votosBolsonaro > votosLula and votosBolsonaro > votosCiro:
                        print(f'O presidente eleito foi Bolsonaro com o total de {votosBolsonaro} votos \n')
                    elif votosLula > votosBolsonaro and votosLula > votosCiro:
                        print(f'O presidente eleito foi Lula com o total de {votosLula} votos \n')
                    elif votosCiro > votosLula and votosCiro > votosBolsonaro:
                        print(f'O presidente eleito foi Ciro com o total de {votosCiro} votos \n')
                    elif votosCiro == votosLula and votosCiro > votosBolsonaro and votosLula > votosBolsonaro:
                        print('A votação será decidida no segundo turno entre Ciro e Lula!')
                    elif votosBolsonaro == votosLula and votosBolsonaro > votosCiro and votosLula > votosCiro:
                        print('A votação será decidida no segundo turno entre Bolsonaro e Lula!')
                    elif votosBolsonaro == votosCiro and votosBolsonaro > votosLula and votosCiro > votosLula:
                        print('A votação será decidida no segundo turno entre Bolsonaro e Ciro!')
                    else:
                        pass
                    
                    # Resultado
                    print("NÚMERO TOTAL DE VOTOS: \n")
                    print(f'[on green]Bolsonaro:[/] {votosBolsonaro}')
                    print(f'[on blue]Ciro:[/] {votosCiro}')
                    print(f'[on red]Lula:[/] {votosLula}')
                    print(f'[on black]Nulos:[/] {nulo}')
                    print(f'[on white]Branco:[/] {branco}')
                    break
                elif finalizar == 2:
                    os.system('cls')
                    continue
                else:
                    pass                
    except:
        os.system('cls')
        print('\n Digite apenas números para escolher o seu candidato. \n Por favor, vote novamente! \n')