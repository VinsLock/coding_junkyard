def specialArray(nums):
    t = len(nums)
    for i in range(t+1):
        tot=0
        for j in nums:
            if j>=i:
                tot+=1
        if i==tot:
            return tot
    
    return -1

print(specialArray([3,5]))