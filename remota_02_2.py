# -*- coding: utf-8 -*-
"""remota_02_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MoQR3-WSCqSWGFIaMAkgq3onmVF4W0Xo
"""

def teclado(a):
  return ord(a)

def main():
  caractere = input('Digite um caractere para saber seu número correspondente: ')
  codigo = teclado(caractere)
  print(f'O código numérico correspondente ao caractere lido é: {codigo}')

if __name__=='__main__':
  main()