def palin(x):
    n = str(x)
    if n == n[::-1]:
        return 'true'
    else:
        return 'false'  
    
if __name__ == '__main__':
    x = int(input())
    print(palin(x))