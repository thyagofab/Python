def escreva(msg):
    print("~"*(len(msg) + 4))
    print(f'{f" {msg}":^{len(msg)}}')
    print("~"*(len(msg) + 4) )

escreva("Gustavo Guanabara")
escreva("CURSO DE PYTHON NO YOUTUBE")
escreva("CeV")