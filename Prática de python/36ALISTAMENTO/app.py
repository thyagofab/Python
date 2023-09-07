""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
I = int(input("Seu ano de nascimento: "))
A = date.today().year
ID = A - I
if ID == 18:
    print("Você tem que se Alistar!")
    print(f"Quem nasceu em {I} tem {ID} anos em {A}")
elif ID < 18:
    print("você ainda não pode se alistar!")
    N = 18 - ID
    S = A + N
    print(f"Falta Ainda {N} anos para se alistar")
    print(f"Quem nasceu em {I} tem {ID} anos em {A}")
    print(f"Seu alistamento será em {S}")
elif ID > 18:
    print("Você já passou do alistamento e vai pagar multa e tem que se apresentar")
    N = ID - 18
    print(f"Você está atrasado com exercito {ID - 18} anos")
    print(f"Quem nasceu em {I} tem {ID} anos em {A}")
    print(f"Seu alistamento foi {(A - N)} ")
