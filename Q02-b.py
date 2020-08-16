def media(a, b, c, d):
    return a, b, c, d

def main(): 
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    media = (num_1 + num_2 + num_3) / 3
    print(f'{media}')
    
if __name__=='__main__':
    main()
