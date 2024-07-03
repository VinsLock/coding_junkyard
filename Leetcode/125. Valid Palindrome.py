def isPalindrome(s):
    s = s.lower()
    ans=''
    for i in s:
        if i.isalnum()==True:
            ans+=i
    return ans==ans[::-1]
    
    
    
print(isPalindrome("A man, a plan, a canal: Panama"))