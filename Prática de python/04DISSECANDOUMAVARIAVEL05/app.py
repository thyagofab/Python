nome= input("DIGITE ALGO: ")
print(f"O TIPO PRIMITIVO DIGITADO É {type(nome)}")
print(f"SÓ TEM ESPAÇO? {nome.isspace()}")
print(f"É UM NÚMERO? {nome.isnumeric()}")
print(f"É ALFABÉTICO? {nome.isalpha()}")
print(f"É ALFANUMÉRICO? {nome.isalnum()}")
print(f"ESTÁ EM MAÍSCULAS? {nome.isupper()}")
print(f"ESTÁ EM MÍNUSCULAS?{nome.islower()}")
print(f"ESTÁ CAPITALIZADA? {nome.istitle}")