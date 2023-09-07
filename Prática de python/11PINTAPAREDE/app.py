# largura = float(input("DIGITE A LARGURA DA PAREDE: "))
# altura = float(input("DIGITE A ALTURA DA PAREDE: "))
# print(f"SUA PAREDE TEM DIMENSÃO DE {largura}x{altura} E SUA ÁREA É DE {largura*altura}m²")
# print(f"PARA PINTAR ESSA PAREDE, VOCÊ PRECISARÁ DE {(largura*altura)/2:5.2f}L DE TINTA.")

#adaptado

casa = []
comandos = dict()
soma = 0
print("CALCULANDO O TOTAL DE TINTAS PARA PINTAR O COMANDO TODO")
print("-="*40)
n = int(input("DIGITE O TOTAL DE PAREDE DO COMANDO: "))
nome = str(input("DIGITE O NOME DO COMANDO: "))
print("-="*40)
for i in range(0,n):
    comandos.clear()
    comandos['LARGURA'] = float(input("DIGITE A LARGURA DA PAREDE: "))
    comandos['ALTURA'] = float(input("DIGITE A ALTURA DA PAREDE: "))
    comandos['ÁREA M²'] =  comandos['LARGURA'] *comandos['ALTURA']
    comandos['LTINTA'] = comandos['ÁREA M²'] / 2
    casa.append(comandos.copy())
    print("-="*40)
print("PAREDE ", end='')
#TITUTLOS:
for i in comandos.keys():
    print(f'{i:<15}',end='')
print()
print("-="*40)
#VALORES DAS CHAVES:
for k,v in enumerate(casa):
    print(f'{k + 1:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<13}', end='')
    print()
print("-="*40)
for i in range(len(casa)):
    soma += casa[i]['LTINTA']
print(f"O TOTAL DE TINTA PARA PINTAR O COMANDO {nome.upper()} TODO É DE: {soma} LITROS")
