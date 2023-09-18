#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista = []
 # utiliza dois loops "for" para percorrer cada posição da matriz e solicitamos ao usuário que digite um valor para cada posição.
for i in range(0,3):
     linha = [] #criar uma lista dos valores
     for p in range(0,3):
         n = (int(input(f"Digite os valores [{i},{p}]: ")))
         linha.append(n) #Os valores são adicionados a cada linha personalizada
     lista.append(linha) #linha completa é adicionada à lista
    
# Por fim, imprimimos a matriz na tela, percorrendo cada elemento e exibindo-o entre colchetes.
for  i in range(0,3):
     for p in range(0,3):
         print(f'[{lista[i][p]}]',end=' ')
     print()