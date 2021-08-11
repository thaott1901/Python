import numpy as np


def productExceptSelf(nums):
    res = np.ones(len(nums))
    for i in range(len(nums)):
        print("-------------")
        print(res)
        temp = res[i]
        res = res * nums[i]
        res[i] = temp
        print(res)
        print("-------------")
    return res


input = [1, 2, 3, 4]
output = productExceptSelf(input)
print(output)
