from logging import exception
from funcoes import procura_chaves, imprime_contatos, carregar_contatos, guardar_contatos

print("*"*28)
print("*"*10 + "CONTATOS" + "*"*10)
print("*"*28)

contatos = carregar_contatos()

comando = "continue"

while comando != "sair":
    
    comando = input("\nDigite o comando: (novo, pes, sair): ")    
    
    if comando == "novo":
        nome = input("\nNome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()

        contatos[nome.lower()] = {
            "Nome": nome,
            "Telefone": telefone,
            "E-mail": email
        }

        guardar_contatos(contatos)

    if comando == "pes":
        nome = input("\nNome: ").lower()
        chaves_encontradas = procura_chaves(contatos, nome)

        if len(chaves_encontradas) > 0:
            imprime_contatos(contatos, chaves_encontradas)
        else:
            print("Nenhuma correspondência encontrada")
    
    if (comando != "novo" and comando != "pes" and comando != "sair"):
        print("\nEscolha um comando válido")
    
    if comando == "sair":
        print("\nPrograma finalizado")