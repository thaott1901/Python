import numpy as np


def productExceptSelf(nums):
    size = len(nums)
    index = size - 1
    # build prefix array (accumulated value before ith element)
    frontArr = [1] * size
    for i in range(size):
        if i == 0:
            frontArr[i] = 1
        else:
            frontArr[i] *= frontArr[i - 1] * nums[i - 1]
    # build suffix array (accumulated value before ith element)
    backArr = [1] * size
    reverse = nums[::-1]
    for i in range(size):
        if i == 0:
            backArr[i] = 1
        else:
            backArr[i] *= backArr[i - 1] * reverse[i - 1]
    # multiply both array element wise
    res = [1] * size
    for i in range(size):
        res[i] = frontArr[i] * backArr[index - i]

    return res


input = [1, 2, 3, 4]
output = productExceptSelf(input)
print(output)

