import tkinter as tk
from escolher import g_numero
from interface import FrameSenha

app = tk.Tk()

menu = FrameSenha(app)
menu.func = g_numero

app.mainloop()


"""
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
main()
"""
