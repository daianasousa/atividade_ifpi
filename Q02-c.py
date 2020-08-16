def cubo(num, calculo):
    return num, calculo

def main():    
    num = int(input())
    calculo = (num ** 3)
    print(f'{calculo}')
    
if __name__=='__main__':
    main()
