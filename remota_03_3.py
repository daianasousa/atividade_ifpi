def verde(a):
  return f'SIGA!'

def amarelo(b):
  return f'ATENÇÃO!'

def vermelho(c):
  return f'PARE!'

def main():
  cor = str(input('Digite uma das cores de sinal de trânsito. "V" é verde / "A" é amarelo / "E" é vermelho: ')).upper()
  cores_1 = verde(cor)
  cores_2 = amarelo(cor)
  cores_3 = vermelho(cor)

  if cor == 'V':
    print(f'{cores_1}')
  elif cor == 'A':
    print(f'{cores_2}')
  elif cor == 'E':
    print(f'{cores_3}')
  else:
    print('Opção Invalida. Somente aceita entre V, A, E!')
    
if __name__=='__main__':
  main()  
