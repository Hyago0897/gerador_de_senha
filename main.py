import random, time
from . import *
from os import system


def gerador(quant_caracter):
    senha = ""
    for c in range(quant_caracter):
        senha = senha + str(random.randint(0,9))
    
    return senha


def menu():
        quant_caracter = int(input("Informe a quantidade de caracteres da senha: "))

        print("GERANDO SENHA")

        senha = gerador(quant_caracter)

        print("SENHA GERADA COM SUCESSO!")

        print(f'A SENHA GERADA É: {senha}')

        time.sleep(2)


def main():
    while True:
        system("cls")

        print("GERADOR DE SENHA")

        menu()

        continuar = input("Deseja gerar uma senha? ")

        if continuar.lower() == 'n':
            exit()
        

print(especiais)

main()