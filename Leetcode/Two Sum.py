def twosum(nums, target):
    dict={}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in dict:
            return [i,dict[temp]]
        dict[nums[i]] = i

    