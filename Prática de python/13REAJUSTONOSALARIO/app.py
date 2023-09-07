#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#jeito 01
#salario = float(input("QUAL É O SALÁRIO DO FUNCIONÁRIO? R$"))
#print(f"UM FUNCIONÁRIO QUE GANHAVA R${salario}, COM 15% DE AUMENTO, PASSA A RECEBER R${salario + (salario*0.15):.2f}")

#jeito 02
op = 's'
n = dict()
while op != 'N':
    print("-="*30)
    n['NOME'] = str(input("DIGITE SEU NOME: "))
    n['SALARIO'] = float(input("DIGITE SEU SALÁRIO:R$ "))
    n['DESCONTO'] = float(input("DIGITE O DESCONTO DE AUMENTO %: "))
    print(f"OLÁ Sr.(a) {n['NOME'].upper()} seu salário anterior era de {n['SALARIO']}R$, com o aumento de {n['DESCONTO']}%,passa a receber R${n['SALARIO'] + (n['SALARIO']*(n['DESCONTO']/100)):.2f}")
    op = str(input("DESEJA CONTINUAR [S/N]: "))[0].strip().upper()
print("-="*30)
print("VLW, POR USAR MINHA CALCULADORA DE DESCONTO VOLTE SEMPRE.")