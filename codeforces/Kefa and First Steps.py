n = input()
l = list(map(int,input().split()))

ans=1
max=1
for i in range(1,len(l)):
    if l[i-1]<=l[i]:
        ans+=1
        if ans>max:
            max=ans
    else:
        ans=1
    
print(max)