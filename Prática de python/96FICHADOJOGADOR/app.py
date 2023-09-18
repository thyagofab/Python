def ficha(nome = '<DESCONHECIDO>', gols = 0):
    print(f"O JOGADOR {nome} FEZ {gols} GOL(S) NO CAMPEONATO")

n = str(input("NOME DO JOGADOR: ")).upper()
g = str(input("NÚMERO DE GOLS: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)