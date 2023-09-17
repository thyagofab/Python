# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n = 0
while n != 5:
    print("=-"*20)
    print("---- NÚMEROS DESEJADOS ----")
    print("=-"*20)
    N1 = float(input("Digite um número: "))
    N2 = float(input("Digite o segundo número: "))
    print("=-"*20)
    print("""----------MENU-----------
  [1] - SOMA    
  [2] - MULTIPLICAÇÃO   
  [3] - MAIOR
  [4] - NOVOS NÚMEROS   
  [5] - SAIR DO PROGRAMA  
  -------------------------""")
    n = int(input("Digite a opção acima: "))

    if n == 1:
        print("=-"*20)
        soma = N1 + N2
        print(f"Soma {N1} e {N2} é igual {soma}")
        print("=-"*20)
    elif n == 2:
        print("=-"*20)
        multi = N1 * N2
        print(f"A multiplicação dos números {N1} e {N2} é igual á {multi}")
    elif n == 3:
        if N1 > N2:
            print(f"O número {N1} é maior do que {N2}")
        else:
            print(f"O número `{N2} é maior do que {N1}")
    elif n == 4:
        print("=-"*20)
        print("Digitar novos números!")
        print("=-"*20)
    elif n == 5:
        print("Vlw, por usar meu programa!")
    else:
        print("opção inválida. tente novamente!")
print("=-"*20)
print("volte sempre. teminamos o programa!")
print("=-"*20)
