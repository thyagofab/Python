def area(largura,comprimento):
    area = largura*comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {area:.2f} m²")
print(f'{"CONTROLE DE TERRENOS":^40}')
print("--"*20)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura,comprimento)
