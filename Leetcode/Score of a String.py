def scoreOfString(s):
    a = []
    for i in s:
        a.append(ord(i))
    ans = 0
    for i in range(1,len(a)):
        print([a[i-1],a[i]])
        ans+=abs(a[i-1]-a[i])
    print(a)
    return ans

print(scoreOfString('hello'))

