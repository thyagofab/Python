# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

pares = []
impa = []
lista = []

while True:
    lista.append(int(input("Digite o número: ")))
    op = ' '
    while op not in "SN":
        op = str(input("Quer continuar: ")).strip().upper()[0]
    if op == 'N':
        break
# i é a posição que número se encontra e v é o valor do número digitado
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impa.append(v)
