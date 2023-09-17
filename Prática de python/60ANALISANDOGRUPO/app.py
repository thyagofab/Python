# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos

M18 = 0
Ho = 0
Mu = 0
while True:
    print("--"*20)
    print("CADASTRE UMA PESSOA")
    print("--"*20)
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip().upper()[0]
    if idade > 18:
        M18 += 1
    while sexo not in 'MFmf':
        sexo = str(input("SEXO [M/F]: ")).strip().upper()[0]
        print("--"*20)
    if sexo == "M":
        Ho += 1
    if idade < 20 and sexo == 'F':
        Mu += 1
    print("--"*20)
    R = str(input("QUER CONTINUAR [S/N]: ")).strip().upper()[0]
    while R not in "SNsn":
        R = str(input("QUER CONTINUAR [S/N]: ")).strip().upper()[0]
    print("--"*20)
    if R == "N":
        break
print("====== FIM DO PROGRAMA ======")
print(f"""Total de pessoas com mais de 18 anos: {M18}
 Ao todo temos {Ho} homens cadastrados
 E temos {Mu} mulheres com menos de 20 anos""")
