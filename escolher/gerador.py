import random
from tkinter import BooleanVar


class GeradorSenha():
    def __init__(self, quant=8) -> None:
        self.senha = None

    @property
    def senha(self) -> str or bool:
        if self._senha is None:
            return bool(0) or False
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def gerar(self, quant=8):
        caracteres = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ!@#$%¨&*()£¢¬_-+=§`´[{]}~^?/°:;>.<,\\|'\""
        senha = ""
        for _ in range(quant):
            senha += random.choice(caracteres)

        self.senha = senha

    def __str__(self) -> str:
        return f"{self.senha}"


if __name__ == "__main__":
    t = GeradorSenha(8)
    # t.gerar()
    print(t.senha)
