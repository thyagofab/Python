#calcular a hipotenusa:
from math import sqrt
coposto = float(input("COMPRIMENTO DO CATETO OPOSTO: "))
cadjacento = float(input("COMPRIMENTO DO CATETO ADJACENTO: "))
hipotenusa = sqrt((coposto**2) +(cadjacento**2))
print(f"A HIPOTENUSA VAI MEDIR {hipotenusa:.2f}")
