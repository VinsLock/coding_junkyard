n = int(input())
ans = {}
for i in range(n):
    a = input()
    if a in ans:
        ans[a]+=1
    else:
        ans[a]=1

print(max(zip(ans.values(),ans.keys()))[1])