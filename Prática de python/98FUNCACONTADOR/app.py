#ESCREVA UM PROGRAMA QUE POSSUI UMA FUNÇÃO CONTADOR, NA QUAL IRÁ RECEBER TRÊS PARAMETROS
#INICIO, FIM, PASSO

from time import sleep 
def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("-="*30)
    print(f"CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}")
    if fim > inicio:
        for i in range(inicio,fim+1,passo):
            print(i,end=' ',flush=True)#fush para ir pulando de 1 e 1 o tempo
            sleep(0.3)
    elif inicio > fim:
        for i in range(inicio,fim-1,-passo):
            print(i,end=' ',flush=True)
            sleep(0.3)
    print("FIM")

contador(1,10,1)
contador(10,0,2)
print("-="*30)
print("A AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM")
inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))
contador(inicio,fim,passo)

