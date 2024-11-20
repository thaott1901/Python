from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        start_num = [i for i, num in enumerate(nums) if num == 0]
        res = 0
        for i in start_num:
            balance = abs(sum(nums[:i]) - sum(nums[i + 1:]))
            if balance == 0:
                res += 2
            elif balance == 1:
                res += 1
        return res
    
# Testing
solution = Solution()
tests = [[1,0,2,0,3],[2,3,4,0,4,1,0]]
answer = [2, 0]
res = []
for test, answer in zip(tests, answer):
    temp_res = solution.countValidSelections(test)
    res.append([temp_res, temp_res == answer])
print(res)
