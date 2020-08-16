def conversao(h, m, s, c1, c2, c3):
    return h, m, s, c1, c2, c3

def main():
    hora = int(input())
    minuto = int(input())
    segundo = int(input())
    conversão_1 = (hora * 3600)
    conversão_2 = (minuto * 60)
    calculo = (conversão_1 + conversão_2 + segundo)
    print(f'{calculo:.1f}')

if __name__=='__main__':
    main()



