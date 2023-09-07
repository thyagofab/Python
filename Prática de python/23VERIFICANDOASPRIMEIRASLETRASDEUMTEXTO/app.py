#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

#modelo 01

# cidade = str(input("QUAL CIDADE VOCÊ MORA? ")).strip().upper()
# print((cidade[:5] == 'SANTO'))

#outromodelo
cidade = str(input("QUAL CIDADE VOCÊ MORA? ")).strip().upper()
if cidade in 'SANTO':
    print("SE ENCONTRA SANTOS NO NOME DA CIDADE")
else:
    print("NÃO SE ECONTRA SANTOS NA CIDADE ")