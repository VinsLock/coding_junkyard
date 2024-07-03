a,b = map(int,input().split())
l = list(map(int,input().split()))
m = max(l)
for i in range(0,b-a+1):
    temp = max(l[i:a+i]) - min(l[i:a+i]) 
    if temp<m:
        m=temp
    print(l[i:a+i],temp,m)
print(m)



