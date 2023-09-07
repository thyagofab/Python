
"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""
print("-=-"*20)
print(f"{'ANALISADOR DE TRIÂNAGULO':^50}")
print("-=-"*20)

N1 = float(input("Primeiro segmento: "))
N2 = float(input("Segundo segmento: "))
N3 = float(input("Terceiro segmento: "))

if N1 < N2 + N3 and N2 < N1 + N3 and N3 < N1 + N2:
    print("Os segmentos acima PODEM FORMAR triângulo! ")
else:
    print("Não dar para fazer um triângulo!")