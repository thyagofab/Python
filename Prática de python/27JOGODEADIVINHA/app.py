from time import sleep
from random import randint
print("\033[33m-=\033[m"*30)
print("\033[34m VOU PENSAR UM NÚMERO ENTRE 0 E 5. TENTE ADIVINHAR.. \033[m")
print("\033[33m-=\033[m"*30)

digito = int(input("DIGITE O NÚMERO QUE ESTOU PENSANDO: "))
computador = randint(1,5)
print("\033[33mPENSANDO O NÚMERO...\033[m")
sleep(0.5)


if digito == computador:
   print("\033[33m PARABÉNS! VOCÊ CONSEGUIU ME VENCER! \033[m")
else:
   print(f"\033[31m VOCÊ ERROU, EU PENSEI NO NÚMERO {computador}\033[m")