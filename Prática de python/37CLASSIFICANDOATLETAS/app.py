"""A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:"""
from datetime import date
N = int(input("Digite seu ano de nascimento: "))
A = date.today().year
N1 = A - N
if N1 <=9:
    print("Categória Mirim")
elif N1 > 9 and N1 <=14:
    print("Categória infantil")
elif N1 > 14 and N1 <= 19:
    print("categoria Junior")
elif N1 <=25:
    print("Categoria Sênior")
else:
    print('categoria Master')