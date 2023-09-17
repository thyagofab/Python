total = mais = barato = vezes = 0
nomebarato = ''
print("--"*20)
print("LOJA SUPER BARATÃO")
print("--"*20)
while True:
    print("--"*20)
    nomepro = str(input("NOME DO PRODUTO: ")).strip()
    preco = float(input("PREÇO: R$"))
    print("--"*20)
    vezes += 1
# total das compras
    total += preco
# preços mais de 1000
    if preco > 1000:
        mais += 1
# nome do produto mais barato!
    if vezes == 1:
        barato = preco
        nomebarato = nomepro
    elif barato > preco:
        barato = preco
        nomebarato = nomepro
# Caso erre a digitação!
    op = str(input("QUER CONTINUAR [S/N]: ")).strip().upper()[0]
    while op not in "SsNn":
        op = str(input("QUER CONTINUAR [S/N]: ")).strip().upper()[0]
    if op == 'N':
        break
    print("--"*20)

# print("------FIM DO PROGRAMA------")
# print(f"""O total da compra foi R${total}
# Temos {mais} produtos custando mais do que R$1000.00
# O produto mais barato foi {nomebarato} que custa R${barato}""")
