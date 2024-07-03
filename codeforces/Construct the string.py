n=int(input())
s=input()
a=[s[i:i+2] for i in range(n-1)]
print(a)
print(a.count)
print(max(a,key=a.count))