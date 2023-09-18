#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
while True:
    lista.append(int(input("Digite um valor: ")))

    op = ' '
    while op not in "SN":
        op = str(input("QUER CONTINUAR [S/N]: ")).strip().upper()
    if op == "N":
        break
print("-="*30)
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"os valores em ordem decrescente são {lista}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista e está na posição {lista.index(5)}")
else:
    print("O valor 5 não faz parte da lista")