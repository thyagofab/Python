def fatorial(n = 0, show=False):
    """
    -> CALCULE O FAOTRIAL DE UM NÚMERO.
    :Param n: 0 npumero a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: 0 valor do fatorial de um número n.
    """
    f = 1
    for i in range(n, 1 , -1):
        if show: #se show for veradeiro vai mostrar as contas!
            print(f"{i}" ' X ' if i > 0  else ' = ', end=' ')
        f *= i
    return f

n = int(input("DIGITE O NÚMERO DESEJADO: "))
op = str(input("DESEJA QUE MOSTRE AS CONTAS: ")).strip().upper()[0]

if op == 'S':
    print(fatorial(n,True))
elif op == 'N':
    print(fatorial(n,False))
else:
    help(fatorial)