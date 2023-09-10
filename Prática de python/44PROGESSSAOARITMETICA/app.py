"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
P = int(input("Digite o primeiro termo da PA: ")) # aqui você digita o primeiro termo da PA
R = int(input("Digite a razão da PA: ")) #aqui você digita a razão da PA
N = int(input("Digite o número de termo gerado desejado: ")) # aqui é total que digito que é para gerar na PA


#usado no outro modelo:
# d = P + (10 -1) * R #formula para chegar aos dez termos que quer

for i in range(N):
    an = P + i * R # formula da p
    print(an, end=' ')

#outro jeito de fazer:

# for c in range(P, d + R, R):
#     print(c, end="-> ")

print("Acabou")