#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

soma = soma2 = 0
lista = []
for i in range(0,3):
     linha = []
     for p in range(0,3):
         n = int(input(f"Digite um valor [{i},{p}]: "))
         linha.append(n)
     lista.append(linha)
print("-="*20)
for i in range(0,3):
     for p in range(0,3):
         print(f"[ {lista[i][p]} ]",end='')
     print()
print("-="*20)
# #soma da terceira coluna
soma = lista[0][2] + lista[1][2] + lista[2][2]
print(f"A soma dos valores da terceira coluna é {soma}")
#maior valor da segunda coluna
maior = max(lista[1])
print(f"o maior número da segunda linha é {maior}")

# # descobrir um número par em uma lista:
# #utilizamos o for aninhados para cada elemento da lista ai serve para mostrar os pares ou inserrir um lista ou até mesmo para somar eles
for i in lista:
     for p in i:
         if p%2 == 0: #soma dos pares
             soma2 += p
print(f"A soma dos valores pares é {soma2}")