#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
jogo = []
tot = 1
q = int(input("Quantos jogos você quer: "))
while tot <= q:
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont +-1 
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3,f' SORTEANDO {q} JOGOS ', '-='*3)
for i, l in enumerate(jogo):
    sleep(0.5)
    print(f'jogo {i + 1}: {l}')