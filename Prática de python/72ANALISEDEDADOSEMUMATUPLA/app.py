#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n = (int(input("DIGITE UM VALOR: ")),
     int(input("DIGITE OUTRO VALOR: ")),
     int(input("DIGITE MAIS UM VALOR: ")),
     int(input("DIGITE O ÚLTIMO NÚMERO: ")))

print(f"você digitou os valores {n}")
print(f"O valor 9 apreceu{n.count(9)} vezes")
if 3 in n:
    # mais para desconsiderar os zeross e dizer posição correta.
    print(f"o valor 3 apareeu {n.index(3) + 1}° posição")
else:
    print("O VALOR 3 NÃO FOI DIGITADO NENHUM POSIÇÃO")
print("os valores pares foram: ")
for i in n:
    if n % 2 == 0:
        print(n, end=' ')
