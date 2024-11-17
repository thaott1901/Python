from typing import List
class Jump:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i in range(len(nums)):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + nums[i])
        return True

jump = Jump()
nums = [2, 3, 1, 1, 4]
res = jump.canJump(nums)
print(res)