def num(a):
  return True

def dois(b):
  return False

def main():  
  caractere = str(input('Escreva na tela um caractere: '))
  parametro = num(caractere)
  passo = dois(caractere)

  if caractere >= '0' and caractere <= '9':
    print(parametro)
  else:
    print(passo)    

if __name__=='__main__':
  main()
