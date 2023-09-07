#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
#jeito 1:
#preco = float(input("QUAL É O PREÇO DO PRODUTO? R$"))
#print(f"O PRODUTO QUE CUSTAVA R${preco}, NA PROMOÇÃO COM DESCONTO DE 5% VAI CUSTAR R${preco-(preco*0.05):.2f}")

#jeito mais rápido e prático:
while True:
    print("-="*30)
    nome =str(input("QUAL NOME DO PRODUTO? "))
    preco = float(input("QUAL É O PREÇO DO PRODUTO? R$"))
    desconto = float(input("QUAL É A % DE DESCONTO DADO? "))
    print(f"O PRODUTO {nome} QUE CUSTAVA R${preco}, NA PROMOÇÃO COM DESCONTO DE {desconto}% VAI CUSTAR R${(preco-(preco *(desconto/100))):.2f}")
    op = ' '
    if op not in "SN":
        op =str(input("DESEJA CALCULAR NOVAMENTE: "))[0].strip().upper()
        if op == 'N':
            break
print("VLW,POR USAR MINHA CALCULADORA DE DESCONTO VOLTE SEMOPRE :3")