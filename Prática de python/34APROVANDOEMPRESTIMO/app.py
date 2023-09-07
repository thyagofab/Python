"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valor_casa = float(input("Qual valor da casa? "))
salario = float(input("Qual é seu salário?  "))
anos = int(input("Em quantos anos você vai pagar? "))

m = anos * 12
p = valor_casa / m
x = salario *0.3

if p > x:
     print("Infelizmente, você não pode financiar essa casa. ", end='')
     print(f"A prestação das parcelas da casa é de R${p:.2f} em {anos} anos, assim cedeu mais que 30% do seu salário")
else:
     print("Parabéns, você conseguiu Aprovação do emprestimo de financiamento da casa!", end='')
     print(f"A prestação das parcelas da casa é de R${p:.2f} em {anos} anos")