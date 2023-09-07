"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido"""
from random import choice
nomes = []
for i in range(1,5):
    nomes.append(str(input(f"NOME DO ALUNO {i}º: ")))
print(f"O ALUNO ESCOLHIDO {choice(nomes)}")