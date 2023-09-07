from random import randint
numeros = []
def sorteio():
    for i in range(0, 5):
        numeros.append(randint(1,10))
    print(f"SORTEANDO 5 VALORES DA LISTA: {numeros}")
def somapar(*valores):
    s = 0
    for n in range(0, len(valores)):
        if valores [n] % 2 == 0:
            s += valores [n]
    print(f"SOMANDO OS VALORES PARES DE {numeros}, temos {s}")

sorteio()
somapar(*numeros) #precisa coloar * para considrar vários números