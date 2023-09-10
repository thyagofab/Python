"""Esse programa tem objetivo de mostrar maior e menor número com sua média de números que foi digitado""" 
r = 'S'
maior = 0
menor = 0 
vezes = 0
soma = 0
while r == 'S':
         n = int(input("Digite o número inteiro desejedo: "))
         r = str(input("Deseja continuar [S/N]: ")).strip().upper()
         soma += n
         vezes += 1 
         if vezes == 1:
                 maior = n
                 menor = n
         else:
                 if n > maior:
                         maior = n
                 if n < menor:
                         menor = n
media = soma / vezes 
print(f"meu maior número é {maior}")
print(f"meu menor número é {menor}")
print(f"A media dos números é {media:.2f}")