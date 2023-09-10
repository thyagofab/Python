""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

velho = 0
media = 0
mulheres = 0
somaidade = 0
nomeh = ''

for dados in range(1,5):
     print("\033[1;31m-=\033[m"*30)
     nome = str(input(f"Digite seu {dados}° nome: ")).strip()
     idade = int(input(f"Digite sua {dados}° idade: "))
     sexo = str(input(f"Digite seu {dados}° sexo masculino ou feminino (M/F): ")).strip().upper()
     print("\033[1;31m-=\033[m"*30)
    
#média de idade:
     somaidade += idade
     media = somaidade / dados
#soma das idade das mulheres de menores:
     if sexo == 'F' and idade < 20: 
         mulheres += 1
#idade do homem mais velho:
     else:
         if sexo == 'M' and dados == 1:
            velho = idade
         elif idade > velho and sexo =='M':
             velho = idade
         if velho == idade:
             nomeh = nome


print("\033[1;31m-=\033[m"*30)
print("RESPOSTA")
print(f"A médiade idade das 4 pessoas é de {media}")
print(f"O nome do homem mais velho é {nomeh} e ele tem {velho} anos")
print(f"O número de mulheres que tem uma idade menos do que 20 anos é de {mulheres}")
print("\033[1;31m-=\033[m"*30)