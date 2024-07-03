n = int(input())
ans=[]
while(n):
    num = int(input())
    a = num%2020
    b = num//2020
    if a<=b:
        ans.append("YES")
    else:
        ans.append("NO")
    
    n-=1
for i in ans:
    print(i)