def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    last = 0
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != prev:
            prev = nums[i]
            last = i
        else:
            nums[i] = "*"
    nums[:] = (value for value in nums if value != "*")