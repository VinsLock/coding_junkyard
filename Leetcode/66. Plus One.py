def plusOne(digits):
    num=''
    for i in digits:
        num+=str(i)
    
    num = list(str(int(num)+1))
    ans = []
    for i in num:
        ans.append(int(i))
    return ans
    
    
    
print(plusOne([9]))