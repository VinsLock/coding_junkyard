n = input()
l = list(map(int,input().split()))
sum_l = sum(l)
l.sort()

check = 0
count = 0
for i in l[::-1]:
    check+=i
    count+=1
    if check>sum_l//2:
        break
print(count)
    