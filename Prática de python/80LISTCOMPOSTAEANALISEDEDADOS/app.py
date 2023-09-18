# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves


lista = list()
dados = list()
maior = menor = 0
# #leitura de dados
while True:
     lista.append(str(input("nome: ")))
     lista.append(float(input("peso: ")))
     #parte de indentificar maior peso:
     if len(dados) == 0: #castrando como não cadastrei nenhum pessoa 
         maior = menor = lista[1] # guarda o primeira pessoa de dados como maior e menor
     else:
         if lista[1] > maior:
             maior = lista[1]
         if lista[1] < menor:
             menor = lista[1]
     dados.append(lista[:])
     lista.clear()
     op = ' '
     if op not in 'SN':
         op = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
     if op == "N":
         break

print(f" o total de pessoas cadastrada{len(dados)}") # total de pessoas cadastradas!!!

print(f"o  maior peso foi de {maior} kg",end=' -> ')
for p in dados:
     if p[1] == maior:
          print(f"{p[0]}", end=' ')
print()
print(f"o  menor peso foi de {menor} kg",end=' -> ')
for q in dados:
     if p[1] == menor:
         print(f"{p[0]}",end=' ')