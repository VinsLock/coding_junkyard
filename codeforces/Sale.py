n,m = map(int,input().split())
tv = list(map(int,input().split()))

tv.sort()
sum=0
for i in range(m):
    if tv[i]<0:
        sum+=abs(tv[i])
    else:
        break
print(sum)