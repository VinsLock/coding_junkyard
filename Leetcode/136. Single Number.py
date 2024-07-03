def singleNumber(nums):
    nums.sort()
    print(nums)
    if len(nums)==1:
        return nums[0]
    i=0
    while(i<=len(nums)-1):
        if i==len(nums)-1:
            return nums[i]
        elif nums[i]==nums[i+1]:
            i+=2
        else:
            return nums[i]
        
        
    
print(singleNumber([2,2,1]))