"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input("INFORME SEU SEXO [M/F]: ")).strip().upper()[0]# esse parentes é para pegar primeira letra caso ele digite masculino ou feminino
while sexo not in 'MmFf': #se em sexo não conter nenhum dessa carcteres entre parentes ele digita novamente!
     sexo = str(input("dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")


