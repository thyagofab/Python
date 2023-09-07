
#modelo 01
# N1 = int(input("Primeiro valor: "))
# N2 = int(input("Segundo valor: "))
# N3 = int(input("Terceiro Valor: "))

# l =[N1, N2, N3]
# l.sort() # ordena os números

# print(f"Maior número é {l[2]} e menor número é {l[0]} ")

#outro jeito de fazer esse programa: 

# N1 = int(input("Primeiro valor: "))
# N2 = int(input("Segundo valor: "))
# N3 = int(input("Terceiro Valor: "))

# # #Verificando o menor número: 

# if N1 < N2 and N1 < N2:
#      menor = N1
# elif N2 < N2 and N2 < N3:
#      menor = N1
# elif N3 < N1 and N3 < N2:
#      menor = N3

# # #Verificando o maior número:

# if N1 > N2 and N1 > N2:
#      maior = N1
# elif N2 > N1 and N2 > N3:
#      maior = N1
# elif N3 > N1 and N3 > N2:
#      maior = N3

# print(f"O menor número é {menor}")
# print(f"O maior número é {maior}")

#modelo 03
maior = 0
menor = 0
for i in range(1,4):
    N1 = int(input(f"digite o valor {i}ª: "))
    if i == 0:
        maior = N1
        menor = N1
    elif N1 > maior:
        maior = N1
    elif N1 < menor:
        menor = N1
print(f"O MAIOR NÚMERO {maior}")
print(f"O MENOR NÚMERO {menor}")