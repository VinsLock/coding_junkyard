def removeElement( nums, val):
    ans = ['' if x == val else x for x in nums]
    while '' in ans:
        ans.remove('')
    return len(ans)

print(removeElement([3,2,2,3],3))