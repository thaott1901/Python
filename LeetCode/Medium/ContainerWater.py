from typing import List
class Container:
    def maxArea(self, height: List[int]) -> int:
        maxarea = left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxarea = max(maxarea, area)
        return maxarea

# Create an instance of the Container class
container = Container()

# Now call maxArea on the instance
arr = [5, 1, 3, 4]
res = container.maxArea(arr)
print(res)