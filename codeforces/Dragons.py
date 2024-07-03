def defeat_the_d(s,n):
    dragons = []

    while(n):
        n-=1
        dragons.append(list(map(int,input().split())))
    dragons.sort()
    for i in dragons:
        if s>i[0]:
            s+=i[1]
        else:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    s,n = map(int,input().split())
    print(defeat_the_d(s,n))