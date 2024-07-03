def lengthOfLastWord(s):
    a = s.split()
    return len(a[-1])
    
print(lengthOfLastWord("Hello World"))