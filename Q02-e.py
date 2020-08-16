def medida(a, b, c, d, e, f):
    return a, b, c, d, e, f

def main():
    a = float(input())
    c = float(input())
    l = float(input())
    area_piso = l * c
    volume_sala = l * c * a
    area_parede = 2 * a * l + 2 * a * c
    print(f'{area_piso:.2f}')
    print(f'{volume_sala:.2f}')
    print(f'{area_parede:.2f}')

if __name__=='__main__':
    main()
