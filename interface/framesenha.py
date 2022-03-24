from cgitb import enable
from os import read
import tkinter as tk
from tkinter import ttk

from click import edit


class FrameSenha(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self._master = master

        self.__func:function = None
        self.__senha:str = any

        self.container1 = tk.Frame(self._master)
        self.container2 = tk.Frame(self._master)
        self.container3 = tk.Frame(self._master)

        self.Labelquant = tk.Label(self.container1, text="Informe a quantidade de caracteres: ")
        self.quant = ttk.Spinbox(self.container1)
        self.criar = tk.Button(self.container2, text="CRIAR SENHA", command=self.exibir_senha)
        self.exibir = tk.Label(self.container3, text="A SENHA GERADA É: ")

        self.Labelquant.grid(row=0, column=0)
        self.quant.grid(row=0, column=1)
        self.criar.pack()
        self.exibir.pack()

        self.container1.pack()
        self.container2.pack(pady=10)
        self.container3.pack()

    @property
    def func(self):
        return self.__func

    @func.setter
    def func(self, func):
        self.__func = func

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def nova_senha(self):
        quant_caracteres = self.quant.get()
        try:
            quant_caracteres = int(quant_caracteres)
            self.senha = self.func(quant_caracteres)
        except ValueError:
            self.senha = self.func()

    def exibir_senha(self):
        self.nova_senha()
        self.exibir.config(text=f"A SENHA GERADA É: {self.senha}")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("400x300")

    FrameSenha(app)

    app.mainloop()