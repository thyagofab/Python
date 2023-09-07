medida = float(input("DIGITE UMA DISTÂNCIA EM METROS: "))
print(f"A MEDIDA DE {medida}m corresponde a")
print(f"{medida/1000}km")
print(f"{medida/100}hm")
print(f"{medida/10}dam")
print(f"{medida*10}dm")
print(f"{medida*100}cm")
print(f"{medida*1000}mm")

#programa adaptado: 

medida = float(input("DIGITE UMA DISTÂNCIA EM METROS: "))
while True:
    print("ESCOLHA UMA OPÇÃO A BAIXO")
    print(f"DISTÂNCIA DIGITADA {medida}m")
    print("-="*30)
    print("| (1) CONVERTER EM KM |")
    print("| (2) CONVERTER EM HM |")
    print("| (3) CONVERTER EM DAM|")
    print("| (4) CONVERTER EM DM |")
    print("| (5) CONVERTER EM CM |")
    print("| (6) CONVERTER EM MM |")
    print("| (7) PARA SAIR       |")
    print("-="*30)
    op = int(input("DIGITE A OPÇÃO: "))
    if op == 1:
        print(f"{medida/1000}KM")
    elif op == 2:
        print(f"{medida/100}HM")
    elif op == 3:
        print(f"{medida/10}DAM")
    elif op == 4:
        print(f"{medida*10}DM")
    elif op == 5:
        print(f"{medida*100}CM")
    elif op == 6:
        print(f"{medida*1000}MM")
    elif op == 7:
        break
    else:
        print("OPÇÃO NÃO EXISTE!!")
    print("-="*30)