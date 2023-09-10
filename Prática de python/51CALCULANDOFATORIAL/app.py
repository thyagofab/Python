"""Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""


usuario = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
contador = usuario
print(f"Calculando... {usuario}! = ", end='')
for fa in range (usuario,1,-1):
      fatorial *= fa
      print(contador,end='')
      print(' x ' if fa > 1  else ' = ', end='')  
      contador -= 1 
print("1", end=' = ')
print(fatorial)

# com while

# usuario = int(input("Digite um número para calcular seu fatorial: "))
# contador = usuario
# f = 1
# while contador > 0:
#     print(contador,end='')
#     print(' x ' if contador > 1 else ' = ', end='')
#     f *= contador
#     contador -= 1
# print(f)
