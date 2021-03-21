def findMedianSortedArrays(nums1, nums2):
    nums3 = nums1
    for num in nums2:
        nums3.append(num)
    nums3.sort()
    mid = len(nums3) // 2
    if len(nums3) % 2 == 1:
        return nums3[mid]
    else:
        return (nums3[mid] + nums3[mid + 1]) / 2

nums1 = [1,3]
nums2 = [2,4]
res = findMedianSortedArrays(nums1, nums2)
print(res)

s = -12345
a = str(abs(s))
b = a[::-1]
print(type(int(b)))
