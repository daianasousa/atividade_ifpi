caractere = str(input('Digite um caractere desejado: ')).lower()
  
if 'a' <= caractere <= 'z':
  print(True) 
elif '0' <= caractere <= '9':
  print(True)
else:
  print(False)
