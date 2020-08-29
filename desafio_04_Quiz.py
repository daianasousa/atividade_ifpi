print('= =' * 25)
print('                       MANTENDO A PONTUAÇAO')
print('= =' * 25)
score = 0

print('''
Q_1 Como se chama a função utilizada para imprimir dados na tela do computador? 
a - variavel
b - print
c - interpretador
''')
questao_1 = input().lower()
if questao_1 == 'b':
    print('Parabéns. Você acertou!')
    score += 1
else:
    print('Que pena você ERROU!')
    

print('''
Q_2 Qual das alternativas abaixo não está armazenado como um float? 
d - 7.0
e - 2.4
f - 7
''')
questao_2 = input().lower()
if questao_2 == 'f':
    print('Parabéns! Você acertou.')
    score += 1
else:
    print('Que pena você ERROU!')
    
    
print('''
Q_3 Qual a saída do código abaixo?
<<< x = 3
<<< x *= 3
print(x)

g - 5
h - 3
i - 12
''')
questao_3 = input().lower()
if questao_3 == 'i':
    print('Parabéns! Você acertou.')
    score += 1
else:
    print('Que pena você ERROU!')
    
    
print('''
Q_4 O que é Python?
j - um conjunto de ferramentas para edição.
k - um ambiente de desenvolvimento.
l - uma linguagem de programação.
''')
questao_4 = input().lower()
if questao_4 == 'l':
    print('Parabéns! Você acertou.')
    score += 1
else:
    print('Que pena você ERROU!')

    
print('''
Q_5 como são chamados os módulos pré-instalados do Python?
m - biblioteca padrão.
n - import
o - math
''')
questao_5 = input().lower()
if questao_5 == 'm':
    print('Parabéns! Você acertou.')
    score += 1
else:
    print('Que pena você ERROU!')

print(f' Sua pontuação foi {score} pontos.')

if score == 5:
  print('Continue assim. Voce foi muito bem! ')

else:
  print('Estude mais! Sua pontuação foi péssima.')

