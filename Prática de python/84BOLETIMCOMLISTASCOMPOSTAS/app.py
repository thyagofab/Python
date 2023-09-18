#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

geral = []
while True:
     nome =(str(input("Nome: ")))
     nota1 = float(input("Nota 1: "))
     nota2 = float(input("nota 2: "))
     me = (nota1 + nota2) / 2
     geral.append([nome,[nota1,nota2], me]) # lista composta para cada pessoa que é cadastrada!
     op = ' '
     if op not in 'SN':
         op = str(input("DESEJA CONTINUAR [S/N]: ")).upper()
     if op == "N":
         break
#se ligue que  é alinhamento 
print('-='* 30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-"*26)
#geral nome de cada um cadastra sua posição e média
for i, a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    op = int(input("MOSTRAR NOTAS DE QUAL ALUNO: (999 INTERROMPE): "))
    if op == 999:
        print("Finalizando")
        break
    if op <= len(geral) - 1:
        print(f"Nota de {geral[op][0]} são {geral[op][1]}")
print("VOLTE SEMPRE!!!1")