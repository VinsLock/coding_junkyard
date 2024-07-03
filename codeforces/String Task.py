a = input().lower()

vowel = 'aeiouy'
ans = []
for i in a:
    if i not in vowel:
        ans.append('.'+i)
print(*ans,sep='')