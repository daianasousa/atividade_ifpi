from random import randint
print(':+' * 24)
print('             TESTE DE ADIVINHAÇÃO!!!')
print(':+' * 24)
score = 0
o = randint(0, 100)
conversao = o % 2
print(f'Me diga se o número {o} é ÍMPAR ou PAR?')
n = input().upper()

if conversao == 0:
  if n == 'PAR':
    print('Parabéns voce ACERTOU. Continue assim!!!')
  if n == 'ÍMPAR':
     print('Que pena voce ERROU. Continue tentando!!!')  

else:
  if n == 'ÍMPAR':
    print('Parabéns voce ACERTOU. Continue assim!!!')
  if n == 'PAR':
     print('Que pena voce ERROU. Continue tentando!!!')
