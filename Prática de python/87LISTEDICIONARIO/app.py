# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média 
dados = dict()
geral = []
mulheres = []
cont = 0
while True:
     print("-="*30)
     dados ['Nome'] = str(input("DIGITE SEU NOME: "))
     while True:
          dados['Sexo'] = str(input("DIGITE SEU SEXO (M/F): ")).upper()[0]
          if dados['Sexo'] in 'MF':
               break
          print("ERRO! Por favor, digite apenas M ou F.")
     dados['Idade'] = int(input("DIGITE SUA IDADE: "))
     geral.append(dados.copy())
     cont += dados['Idade']
     if dados['Sexo'] == 'F':
         mulheres.append(dados['Nome'])
     op = ' '
     while op not in 'SN':
         op = str(input("DESEJA CONTINUAR: ")).strip().upper()
     if op == 'N':
         break
media = cont / len(geral)
print(f"- O grupo tem {len(geral)} pessoas")
print(f"- A média de de idade {media:5.2f} anos")
print(f"- As mulheres cadastradas foram: {mulheres}")
print(f"- Lista das pessoas que estão acima da média: ")
for i in geral:
     if i['Idade'] >= media:
          for k,v in i.items():
               print(f"{k} = {v}", end=' ')
     print()
print(f"{'<< ENCERRADO >>':^40}")
