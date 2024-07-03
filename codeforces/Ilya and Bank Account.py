n = int(input())
if n>=0:
    print(n)
else:
    n = abs(n)
    a = n//10
    b = (n//100)*10+(n%10)
    if a>b:
        print(b*-1)
    else:
        print(a*-1)
    