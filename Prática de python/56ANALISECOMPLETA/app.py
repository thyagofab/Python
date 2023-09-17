# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
maisvellho = ''
contf = 0
for i in range(1, 5):
    print(f"PESSOA {i}")
    nome = str(input("DIGITE SEU NOME: ")).strip().upper()
    idade = int(input("DIGITE SUA IDADE: "))
    sexo = str(input("DIGITE SEU  SEXO: ")).strip().upper()[0]
    soma += idade
    if (i == 1):
        maior = idade
    elif (idade > maior and sexo == 'M'):
        maior = idade
        maisvellho = nome
    elif (idade < 20 and sexo == 'F'):
        contf += 1

print(f"A MÉDIA DE IDADE DO GRUPO É DE {soma/4} ANOS")
print(f"O HOMEM MAIS VELHO {maisvellho}  COM UMA IDADE DE {maior}")
print(f"AO TODO SÃO {contf} MULHERES COM MENOS DE 20 ANOS")
