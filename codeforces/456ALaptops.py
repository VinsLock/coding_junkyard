def fun(laptop):
    for i in range(len(laptop)-1):
        a = laptop[i]
        b = laptop[i+1]
        if a[1]<b[1]:
            return 'Happy Alex'
    return "Poor Alex"
    


n = int(input())
laptop=[]
while(n):
    n-=1
    
    a,b = map(int,input().split())
    laptop.append([a,b])
laptop.sort(reverse = True)
print(laptop)
print(fun(laptop))
    
        





