# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
n = ganhou = 0
computador = randint(0, 20)
print("-=-"*30)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-"*30)

while True:
    n = int(input("DIGA UM VALOR: "))
    escolha = str(input("PAR OU ÍMPAR [P/I]: ")).strip().upper()[0]
    total = computador + n
    print("--"*30)
    print(
        f"você jogou {n} e o computador {computador}. Total de {total} ", end='')
    print('Deu par' if total % 2 == 0 else "Deu impar")
    if escolha == 'P':
        if total % 2 == 0:
            print("--"*30)
            print("VOCÊ GANHOU")
            ganhou += 1
        else:
            print("--"*30)
            print("VOCÊ PERDEU")
            break
    elif escolha == 'I':
        if total % 2 == 0:
            print("--"*30)
            print("VOCÊ PERDEU")
            break
        else:
            print("--"*30)
            print("VOCÊ GANHOU")
            ganhou += 1
    print("--"*20)
    print("vamos jogar novamente...")
    print("--"*20)
print("-=-"*30)
print(f"GAME OVER! VOCÊ VENCEU {ganhou} VEZES")
print("-=-"*30)
