# -*- coding: utf-8 -*-
"""remota_02_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q9RcM6ogyUoLjiaRTEmc_ooDJbtBgZP-
"""

def tempo(b, c, d):
  return f'{b}:{c}:{d}'

def main():
  segundo = int(input(f'Digite a duração de um evento da fábrica em segundos: '))
  horas = segundo // 3600
  resto_horas = segundo % 3600
  minutos = resto_horas // 60
  resto_minutos = segundo % 60
  segundos = resto_minutos
  time = tempo(horas, minutos, segundos)
  print(f'O tempo de duração de um evento na fábrica foi {time}')

if __name__== '__main__':
  main()