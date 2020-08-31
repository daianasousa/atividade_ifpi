caractere = str(input('Digite um caractere desejado: ')).lower()
if caractere in ('a', 'e', 'i', 'o', 'u'):
  print(vogal)

elif caractere in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'):
  print('consoante')

elif '0' <= caractere <= '9':
  print('número')

else:
  print('símbolo')  
