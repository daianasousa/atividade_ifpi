# -*- coding: utf-8 -*-
"""Questão_2_Letra_B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CbZzQflczZEGDTFofibl0c0Lf3fUvOGG
"""

def media(num_1, num_2, num_3, media):
  return num_1, num_2, num_3, media
  
def main():  
  num_1 = int(input('Digite um número: '))
  num_2 = int(input('Digite um número: '))
  num_3 = int(input('Digite um número: '))
  media = (num_1 + num_2 + num_3) / 3
  print(f'A média dos números é: {media:.1f}')

if __name__=='__main__':
  main()