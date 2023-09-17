c = ('\033[m',
     '\033[0;30;41;m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m',
);

def ajuda(nom):
    título(f"ACESSANDO O MANUAL DO COMANDO \'{nom}\'",4)
    print(c[6],end='')
    help(nom)
    print(c[0],end='')


def título(mensagem,cor=0):
    tam = len(mensagem) + 4
    print(c[cor],end='')
    print('~'*tam)
    print(mensagem)
    print('~'*tam)
    print(c[0],end='')


nome = ''
while True:
    título('SISTEMA DE AJUDA DO PYTHON',2)
    nome = str(input("FUNÇÃO OU BIBLIOTECA > "))
    if nome.upper() == "SAIR":
        break
    else:
        ajuda(nome)

título("ATÉ MAIS! ",1)
