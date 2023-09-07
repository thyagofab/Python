""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

print("="*15)
print("\033[1;31;40mCALCULO DE IMC\033[m")
print("="*15)

P = float(input("Digite seu peso (kg): "))
A = float(input("Digite sua altura (m): ")) 

IMC = P / (A**2)


if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print("Peso ideal")
elif IMC >= 25 and IMC < 30: 
    print("Sobrepeso")
elif IMC >= 30 and IMC < 40:
    print("Obesidade")
elif IMC >= 40:
    print("Obesidade mórbida")

print(f"Seu IMC é de: {IMC:.1f}")
