print('''
Q1 - Adivinha o nome da minha mãe.
a - Benevina
b - Anatalia
c - Elice
d - Diana
''')
resposta = input().lower()

if resposta == 'a':
  print(' ): Errou essa nem conheço!!! :( ')
elif resposta == 'b':
  print(' ): Você errou esse é seu sobrenome!!! ):  ') 
elif resposta == 'c':
  print(' (: Parabéns, você acertou!!! :) ')
elif resposta == 'd':
  print(' :( Que pena esse nome é da minha irmã!!! :( ') 
else:
  print(' ): Continue tentando uma hora voce consegue acertar!!! :( ')
