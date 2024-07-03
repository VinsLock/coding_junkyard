n = input()
out = []
out = n.split("WUB")
while '' in out:
    out.remove('')

print(*out,sep=" ")