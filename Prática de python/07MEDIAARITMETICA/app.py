#basico
# nome = str(input("DIGITE SEU NOME: "))
# n1 = float(input("DIGITE SUA 1ª NOTA: "))
# n2 = float(input("DIGITE SUA 2ª NOTA: "))
# print(f"A SUA MÉDIA É DE {((n1+n2)/2):.2f}")

#outra forma melhorada 
geral = []
for i in range(0,3):
    print("MÉDIA ESCOLAR ")
    nome = (str(input("DIGITE SEU NOME: ")))
    nota1 = (float(input("DIGITE SUA 1ª NOTA: ")))
    nota2 = (float(input("DIGITE SUA 2ª NOTA: ")))
    media = (nota1 + nota2) / 2
    geral.append([nome,[nota1,nota2],media])
#bug está aqui
print(f"{'COD':<4}{'NOME':<10}{'MÉDIA'}")
for i, a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')