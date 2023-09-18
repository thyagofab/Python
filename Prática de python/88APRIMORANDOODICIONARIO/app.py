#para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dados = dict()
geral = []
while True:
     dados.clear()
     dados['NOME'] = str(input("DIGITE SEU NOME: "))
     dados['T. PARTIDAS'] = int(input("DIGITE QUANTAS PARTIDAS JOGOU: "))
     gols = [] #uma lista de gol é criada para cada interação 
     cont = 0 #cada interação zera o cont para total
     for i in range(0,dados['T. PARTIDAS']):
         g = int(input(f"QUANTOS GOLS FEZ NA PARTIDA {i + 1 }: "))
         cont += g
         gols.append(g)
     dados['GOLS'] = gols
     dados['TOTAL'] = cont
     geral.append(dados.copy())
     op= ' '
     while op not in 'SN':
        op = str(input("DESEJA CONTINUAR [S/N]: ")).strip().upper()
     if op == 'N':
         break
print("-="*30)
print('COD ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print("-="*30)
#tabela de organização:
for k, v in enumerate(geral):
     print(f'{k:>3}', end=' ')
     for d in v.values():
         print(f'{str(d):<15}', end='')
     print()
print("-="*30)
#levantamento de dados por dados
while True: 
     a = int(input("QUER VER DETALHAMENTO DE QUAL JOGADOR (999 PARA PARAR): "))
     if a == 999:
         break
     if a >= len(geral):
         print("ERRO!, NÃO TEM ESSE JOGADOR")
     else:
          print(f"-- LEVANTAMENTO DO JOGADOR {geral[a]['NOME']} --")
          for i, g in enumerate(geral[a]['GOLS']):
               print(f" => NA PARTIDA {i + 1}, FEZ {gols[i]} GOLS")
          print(f"FOI UM TOTAL DE {geral[a]['TOTAL']} GOLS")
     print('-'*40)
print("<< VOLTE SEMPRE >>")