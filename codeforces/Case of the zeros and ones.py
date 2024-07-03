a = input()
b = input()

stack = []
for i in b:
    if stack and stack[-1]!=i:
        stack.pop()
    else:
        stack.append(i)
print(len(stack))