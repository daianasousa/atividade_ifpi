# -*- coding: utf-8 -*-
"""remota_02_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ukx2aeiRTFnhY2b9fdeMovKO93RZBWty
"""

def maximo(i, j, k, l, m):
  return max(i, j, k, l, m)

def minimo(n, o, p, q, r):
  return min(n, o, p, q, r)

def media(s, t, u, v, w):
  return (s + t + u + v + w) / 5

def main():
  num_1 = int(input('Digite o primeiro número: '))
  num_2 = int(input('Digite o segundo número: '))
  num_3 = int(input('Digite o terceiro número: '))
  num_4 = int(input('Digite o quarto número: '))
  num_5 = int(input('Digite o quinto número: '))
  maior = maximo(num_1, num_2, num_3, num_4, num_5)
  menor = minimo(num_1, num_2, num_3, num_4, num_5)
  aritmetica = media(num_1, num_2, num_3, num_4, num_5)
  print(f'O maior número lido é: {maior}') 
  print(f'O menor número lido é: {menor}')
  print(f'A media é: {aritmetica}')

if __name__=='__main__':
  main()