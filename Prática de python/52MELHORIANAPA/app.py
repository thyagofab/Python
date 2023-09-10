"""perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

print("Melhoria no programa de PA.")
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: ")) 
N = int(input("Quantos termos quer ter na PA: "))
pa = 0
termo = 0 
R = 'S'
while R == 'S':
      while pa < N:
          print(primeiro,end=' -> ')
          primeiro += razao
          pa += 1
      print("PAUSA")
      pa = 0
      R = str(input("\nDeseja continuar[S/N]: ")).strip().upper()
      if R == 'S':
          N = int(input("\nQuantos termos você quer mostrar mais? "))
print("Vlw, por usar meu programa de PA!!!!")