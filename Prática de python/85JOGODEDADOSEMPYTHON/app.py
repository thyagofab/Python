#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
jogador = dict()
valores = list()
valor= list()
for i in range(1,5):
     jogador['n'] = randint(1,6)
     print(f"O JOGADOR {i} TIROU {jogador['n']}")
     valores.append(jogador['n'])
     valor.append(jogador['n'])

print("RANKING DOS JOGADORES: ")  
valores.sort(reverse=True)
for k,i in enumerate(valores):
     print(f"{k +1 }º LUGAR JOGADOR {valor.index(i) + 1} com {i} ")


#outro jeito de fazer: 
from random import randint
from time import sleep
from operator import itemgetter

jog = {'jogador 1': randint(1,6),
       'jogador 2': randint(1,6),
       'jogador 3': randint(1,6),
       'jogador 4': randint(1,6)}
ranking = dict()
print("Valores sorteados: ")
for k,v in jog.items():
     print(f"{k} tirou {v} no dado")
     sleep(1)
ranking = sorted(jog.items(), key=itemgetter(1), reverse= True) #a biblioteca usada serve para colocar em ordem o dicionario usando o número 1 para pegar o lado dos número que é sorteado, assim o revers é para colocar na ordem do maior por menor
#tranforma em forma de lista o resultado e é trada como uma lista:
for i, v in enumerate(ranking):
     print(f"{i+1} lugar: {v[0]} com {v[1]};") # é tratado como uma lista o ranking
     sleep(1)
