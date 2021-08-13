def threeSum(nums):
    size = len(nums)
    res = []
    nums.sort()
    if size < 3:
        return res
    for i in range(size - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, size - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res


nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print(res)