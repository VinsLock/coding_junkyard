def romtoint(s):
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum=0
    prev_num = 0
    for i in s[::-1]:
        num = roman_dict.get(i)
        if num>=prev_num:
            sum+=num
        else:
            sum-=num
        prev_num = num
    return sum
    
if __name__ == '__main__':
    s = input()
    print(romtoint(s))