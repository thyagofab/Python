n = int(input("DIGITE UM NÚMERO INTEIRO: "))
antecessor = n
sucessor = n
print(f"ESSES SÃO OS TRÊS NÚMEROS SUCESSOR DE {sucessor}:")
for i in range(0,3):
    sucessor += 1
    print(sucessor,end=' -> ')
print("FIM")
print(f"\nESSES SÃO OS TRÊS NÚMEROS ANTECESSOR DE {antecessor}:")
for i in range(0,3):
    antecessor -= 1 
    print(antecessor,end=' -> ')
print("FIM")