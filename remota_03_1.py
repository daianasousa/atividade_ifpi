def pessoa(a):
  return f'Ilmo Sr. {a}'

def pessoa_1(b):
  return f'Ilma Sra. {b}'

def main():
    n = str(input('Escreva seu nome: '))
    s = int(input('Qual seu sexo? MASCULINO(1) / FEMININO(2): ' )) 
    nome = pessoa(n)
    nome_1 = pessoa_1(n)

    if s == 1:
      print(f'{nome}')

    else:
      print(f'{nome_1}')

if __name__=='__main__':
    main()
  
