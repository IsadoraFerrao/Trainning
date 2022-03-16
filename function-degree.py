def ler_temperatura():
    C=30
    return calcula_fahrenheit(C)

def calcula_fahrenheit(C):
    F = ((9*C+160)/5)
    return show(F)

def show(F):
    print(F)

ler_temperatura()