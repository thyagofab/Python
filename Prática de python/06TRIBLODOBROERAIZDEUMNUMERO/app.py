import math
soma = 0 
n = int(input("DIGITE UM NÚMERO: "))
print(f"INFORMAÇÃO DO NÚMERO {n}:")
print(f"O DOBRO DE {n} VALE {n*2}")
print(f"O TRIBLO DE {n} VALE {n*3}")
print(f"A RAIZ QUADRADA DE {n} VALE {math.sqrt(n)}")
print(f"O FATORIAL DE {n} VALE {math.factorial(n)}")
for i in range(1,n +1):
    if n % i == 0:
        soma += 1
if soma > 2:
    print(f"O NÚMERO {n} NÃO É UM NÚMERO PRIMO")
else:
    print(f"O NÚMERO {n} É UM NÚMERO PRIMO")