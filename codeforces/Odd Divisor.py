n = int(input())
ans=[]
for z in range(n):
    a = int(input())
    if a%2==0:
        ans.append("NO")
    else:
        ans.append("YES")
for i in ans:
    print(i)