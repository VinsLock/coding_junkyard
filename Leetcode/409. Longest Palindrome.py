from collections import Counter


def longestPalindrome(s):
    x = Counter(s)
    flag=0
    ans = 0
    
    for i in x.values():
        if i%2==0:
            ans+=i
        else:
            ans+=i-1
            flag=1
    return ans+1 if flag!=0 else ans

print(longestPalindrome("abccccdd"))