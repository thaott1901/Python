def searchInsert(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
        if i == len(nums) - 1:
            return i + 1