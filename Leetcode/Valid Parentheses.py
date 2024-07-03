def isValid(s):
    open_list = ["[","(","{"]
    close_list = ["]",")","}"]
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack)>0) and (open_list[pos]== stack[-1]):
                stack.pop()
        else:
            return False
    if len(stack)==0:
        return False
    else:
        return True
            





print(isValid("()"))