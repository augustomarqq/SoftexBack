from tkinter import Grid
from tabulate import tabulate
import os
import json

def procura_chaves(dicionario, nome):
    chaves = []
    for chave in dicionario:
        if chave.startswith(nome):
            chaves.append(chave)
        
    for chave in dicionario:
        if chave.endswith(nome):
            chaves.append(chave)

    return chaves

def imprime_contatos(contatos, chaves):
    table = []
    for chave in chaves:
        table.append([
            contatos[chave]["Nome"],
            contatos[chave]["Telefone"],
            contatos[chave]["E-mail"]
        ])

    print(tabulate(table, headers = ["Nome", "Telefone", "E-mail"], tablefmt="grid"))

def carregar_contatos():
    contatos = {}

    if os.path.exists("contatos.json"):
        with open("contatos.json", "r") as f:
            contatos = json.load(f)

    return contatos

def guardar_contatos(contatos):
    with open("contatos.json", "w") as f:
        json.dump(contatos, f, indent=4)