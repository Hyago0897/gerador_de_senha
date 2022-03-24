import random


def g_numero(quant_caracter=2):
    senha = ""
    for c in range(quant_caracter):
        senha = senha + str(random.randint(0,9))

    return senha