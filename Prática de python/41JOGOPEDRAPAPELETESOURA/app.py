"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import choice
from time import sleep


print(":~:"*20)
print("\033[1;34;40mBEM-VINDO AO JOGO DE JOKENPÔ\033[m")
print(":~:"*20)

print("1 - PEDRA ")
print("2 - PAPEL ")
print("3 - TESOURA ")


V = int(input("Escolha um número: "))

print("PEDRA - PAPEL - TESOURA...")
sleep(2)

lista = [1, 2, 3]
R = choice(lista)

if R == 1 and V == 2:
    print(" \033[1;33;40m VOCÊ GANHOU\033[m")
    print("Computador jogou: PEDRA ")
elif R == 2 and V == 3:
    print(" \033[1;33;40mVOCÊ GANHOU\033[m")
    print("Computador jogou: PAPEL")
elif R == 3 and V == 1:
    print(" \033[1;33;40mVOCÊ GANHOU\033[m")
    print("Computador jogou: TESOURA")
elif R == V:
    print("RESULTADO: EMAPATE")
else:
   print("VOCÊ PERDEU")
   if R == 1:
       print("VOCÊ JOGOU: TESOURA")
       print("COMPUTADOU JOGOU: PEDRA")
   if R == 2:
       print("VOCÊ JOGOU: PEDRA")
       print("COMPUTADOU JOGOU: PAPEL")
   if R == 3:
       print("VOCÊ JOGOU: PAPEL")
       print("COMPUTADOU JOGOU: TESOURA")