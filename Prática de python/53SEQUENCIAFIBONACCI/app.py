"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci"""

vezes = 3
n = int(input('Quantos termos quer mostrar ?: '))
t1 = 0 
t2 = 1
print(f"{t1} -> {t2}", end=' -> ')
while vezes < n:
     sequencia = t1 + t2
     t1 = t2
     t2 = sequencia
     vezes +=1
     print(sequencia, end=' -> ')
print("Acabou")