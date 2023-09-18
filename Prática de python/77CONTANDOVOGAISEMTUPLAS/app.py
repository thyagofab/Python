#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python'
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado'
            'programador', 'futuro')

for i in palavras:
    print(F"\nNA PALAVRA {i.upper()} TEMOS ", end='')
    for letra in i:
        if letra.upper() in 'aeiou':  # pega as palavras só em minusculo se a letra estive na no grupo das vogais ele pega aí que você coloca de letras aí vai pegando a letra desejada!!!
            print(letra, end=' ')
