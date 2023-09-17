# onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

Vezes = 0

computador = randint(0, 10)
jogo = ''
while jogo != computador:
    jogo = int(input("Digite um número que computador está pensando: "))
    Vezes += 1
    if jogo == computador:
        print("Parabens, você acertou o número que eu estava adivinhando!!")
        print(f"Em {Vezes} tentativas!")
    else:
        if jogo < computador:
            print("mais...tente mais uma vez.")
        if jogo > computador:
            print("menos...tente mais uma vez")
