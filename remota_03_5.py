nota_1 = int(input('Digite sua primeira nota: '))
nota_2 = int(input('Digite sua segunda nota: '))
nota_3 = int(input('Digite sua terceira nota: '))
media = (nota_1 + nota_2 + nota_3) / 3

if nota_3 > 8:
  media += 1
  if media > 10:
    media = 10
print(f'{media:0.2f}')  
