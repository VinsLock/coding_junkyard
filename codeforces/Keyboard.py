a = "qwertyuiopasdfghjkl;zxcvbnm,./"
n = input()
word = input()
ans=[]
if n == "R":
    for i in word:
        if a.index(i)==0:
            f = len(a)-1
        else:
            f = a.index(i)-1
        ans.append(a[f])
else:
    for i in word:
        if a.index(i)==len(a)-1:
            f = 0
        else:
            f = a.index(i)+1
        ans.append(a[f])
print(*ans,sep='')

