# -*- coding: utf-8 -*-
"""Questão_2_Letra_C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yWl1xSThvcQ6WZrq4-LM2-3yCF99mA4u
"""

def cubo(num, calculo):
  return num, calculo

def main():  
  num = int(input('Escolha um número: '))
  calculo = (num ** 3)
  print(f'O valor do número elevado ao cubo é: {calculo}')

if __name__=='__main__':
  main()