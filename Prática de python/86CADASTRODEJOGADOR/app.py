# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


gols = []
total = 0
jogador = dict()
jogador['NOME'] = str(input("DIGITE SEU NOME: "))
jogador['TOTAL DE PARTIDA'] = int(input("DIGITE O TOTAL DE PARTIDA: "))
for i in range(jogador['TOTAL DE PARTIDA']):
     gols.append(int(input(f"QUANTOS GOLS NA PARTIDA {i}? ")))
jogador['GOLS'] = gols[:]
jogador['TOTAL DE GOLS'] = sum(gols)
print("-="*30)
for k,v in jogador.items():
     print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {jogador['NOME']} jogou {jogador['TOTAL DE PARTIDA']} partidas")
for t in range(0,len(gols)):
     print(f" => NA PARTIDA {t}, FEZ {gols[t]} GOLS")
print(f"FOI UM TOTAL DE {jogador['TOTAL DE GOLS']} GOLS")
