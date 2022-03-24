import tkinter as tk
from escolher import g_numero, g_letra, GeradorSenha
from interface import FrameSenha

app = tk.Tk()

menu = FrameSenha(app)
menu.senha = GeradorSenha()

app.mainloop()
