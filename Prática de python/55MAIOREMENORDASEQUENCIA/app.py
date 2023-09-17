#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range(1,6):
    n = float(input(f"PESO DA {i} PESSOA: "))
    
    if (i == 1):
        maior = n
        menor = n
    elif (n > maior):
        maior = n
    elif (menor > n):
        menor = n

print(f"O MAIOR PESO DIGITADO: {maior}KG")
print(f"O MENOR PESO DIGITADO: {menor}KG")