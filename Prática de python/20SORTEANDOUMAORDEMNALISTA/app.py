from random import shuffle
from time import sleep
nomes = list()
for i in range(1,5):
    nomes.append(str(input(f"DIGITE O NOME DO {i}º: ")))
sleep(1)
print("SORTEANDO A ORDEM.....")
sleep(1)
print("-="*30)
for n in range(0,len(nomes)):
        print(f" O {n + 1}ª alundo {nomes[n]}")