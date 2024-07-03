n = input()

if n.isupper():
    print(n.lower())
elif n[0].islower() and n[1:].isupper():
    print(n[0].upper()+n[1:].lower())
elif len(n)==1:
    print(n.upper())
else:
    print(n)