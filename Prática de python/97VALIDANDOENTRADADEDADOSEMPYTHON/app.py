def leiaint(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg)) #para digitar dentro da função fora dela
        if n.isnumeric():
            valor = int(n) 
            ok = True
        else:
            print("ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO ")
        if ok:
            break
    return valor



n = leiaint("DIGITE UM NÚMERO: ")
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {n}')