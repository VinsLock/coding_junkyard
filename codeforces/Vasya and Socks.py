n,m = map(int,input())

total = 0
day = 0
while(n>0):
    n-=1
    day+=1
    
    if day%m==0:
        n+=1
    total+=1

