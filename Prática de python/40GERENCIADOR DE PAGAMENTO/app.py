""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

print("-="*20)
print("Como você quer pagar")
print("-="*20)

print("Forma de pagamento")
print("1 - À vista dinheiro/cheque: 10% de desconto")
print("2 - À vista no cartão: 5% de desconto")
print("3 - Em até 2x no cartão: preço normal")
print("4 - Em até 3x ou mais no cartão: 20% de juros ")

E = int(input("Escolha uma opção: "))

if E == 1 or E == 2 or E == 3 or E == 4:
    P = float(input("Valor do produto: "))

if E == 1:
    D = P - (P*0.1)
    print(f"A sua compra de R${P:.2f} vai custar R$ {D} no final") 
elif E == 2:
    D = P - (P*0.05)
    print(f"A sua compra de R${P:.2f} vai custar R$ {D} no final")
elif E == 3:
     D = P
     PA = P/2 
     print(f"Sua compara será parcelada em 2x de R${PA}")
     print(f"A sua compra de R${P:.2f} vai custar R$ {D} no final")
elif E == 4:
    D = P + (P*0.2)
    totalparc = int(input("Quantas parcelas: "))
    PA = D / totalparc
    print(f"Sua compra será parcelada em {totalparc}x de R${PA:.2f}")
    print(f"A sua compra de R${P:.2f} vai custar R$ {D} no final")
else:
    print("Essa opção não existe")
