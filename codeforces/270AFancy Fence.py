n = int(input())
ans=[]
while(n):
    n-=1
    a = int(input())
    b = 360/(180-a)
    if b == int(b):
        ans.append('YES')
    else:
        ans.append("NO")
for i in ans:
    print(i)