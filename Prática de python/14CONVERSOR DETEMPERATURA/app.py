#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# temperatura = float(input("INFORME A TEMPERATURA EM °C: "))
# print(f"A TEMPERATURA DE {temperatura}°C CORRESPONDE A {((temperatura * 1.8) + 32):.2f}°F")

#jeito 02 todos conversor de temperatura:

print("-="*25)
print(f'{"CONVERSOR DE TEMPERATURA":^40}')
print("-="*25)
while True:
    temperatura = float(input(f"INFORME A TEMPERATURA EM °C: "))
    print("""[1] - KELVIN
[2] - FAHRENHEIT
[3] - SAIR""")
    print("-="*25)
    op = int(input("ESCOLHA UMA OPÇÃO: "))
    if op == 1:
        print(f"A TEMPERATURA DE {temperatura}°C CORRESPONDE A {temperatura + 273}°K")
    elif op == 2:
        print(f"A TEMPERATURA DE {temperatura}°C CORRESPONDE A {((temperatura * 1.8) + 32):.2f}°F")
    else:
        print("Volte sempre")
        break