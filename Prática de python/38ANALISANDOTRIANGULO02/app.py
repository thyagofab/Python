"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais"""
print("-=-"*20)
print("ANALISADOR DE TRIÂNAGULO   ")
print("-=-"*20)

N1 = float(input("Primeiro segmento: "))
N2 = float(input("Segundo segmento: "))
N3 = float(input("Terceiro segmento: "))

if N1 < N2 + N3 and N2 < N1 + N3 and N3 < N1 + N2:
    print("Os segmentos acima PODEM FORMAR triângulo! ")
    if N1 == N2 == N3:
        print("Triangulo Equilatero")
    elif N1 == N2 or N1 == N3 or N2 ==N3: # poderia colocar else. para simplificar codigo
        print("Triangulo isóceles")
    if N1 != N2 != N3!= N1:
        print("Triangulo Escaleno")
else:
    print("Não é um trinagulo")