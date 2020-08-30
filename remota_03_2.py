def numero(a):
  return a % 2

def main():
  num_1 = int(input('Escreva um número: '))
  calculo = numero(num_1)

  if calculo == 1:
    print(calculo == 1)
  else:
    print(calculo != 0)

if __name__=='__main__':
  main()
