n = int(input())
l = list(map(int,input().split()))

if n>sum(l):
    print(-1)
elif n==0:
    print(0)
else:
    l.sort(reverse=True)
    count=0
    sum=0
    for i in l:
        sum+=i
        count+=1
        if sum>=n:
            break
    print(count)
    
#31
#6 1 0 4 4 5 1 0 5 3 2 0
