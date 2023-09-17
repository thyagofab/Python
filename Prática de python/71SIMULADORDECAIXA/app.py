# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=-"*20)
print('{:^35}'.format("BANCO TH"))
print("=-"*20)
n = int(input("DIGITE O VALOR QUE QUER SACAR: "))
total = n
c = 50
totac = 0
while True:
    if total >= c:
        total -= c
        totac += 1
    else:
        if totac > 0:
            print(f"total de {totac} cédulas de R${c}")
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        totac = 0
        if total == 0:
            break
print("-="*30)
print("VOLTE SEMPRE!!")
