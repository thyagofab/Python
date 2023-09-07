#usa o despacotamento de paramentro
from time import sleep
def maior (*valores):
    print("-="*30)
    print("ANALISANDO OS VALORES PASSADO....")
    sleep(0.5)
    maior = 0
    for n in valores:
        print(n,end=' ',flush=True)
        sleep(0.5)
        if n > maior:
            maior = n
    print(f"FORAM INFORMADOS {len(valores)} VALORES AO TODO")
    print(f"O MAIOR VALOR INFORMADO FOI {maior}")
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()