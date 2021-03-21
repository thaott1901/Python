import math
def maxAscendingSum(nums):
    maxsum = 0
    sum = 0
    lastnum = -math.inf
    for num in nums:
        if lastnum < num:
            lastnum = num
            sum += num
            if maxsum < sum:
                maxsum = sum
        else:
            lastnum = num
            sum = num
    return maxsum

nums = [100,10,1]
res = maxAscendingSum(nums)
print(res)