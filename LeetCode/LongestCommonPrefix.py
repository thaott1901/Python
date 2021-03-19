def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return strs
    if len(strs) == 1:
        return strs[0]
    i = 1
    res = strs[0]
    while i < len(strs):
        count = 0
        str1 = res
        str2 = strs[i]
        size = min(len(str1), len(str2))
        for j in range(size):
            if str1[j] != str2[j]:
                break
            count += 1
        res = str1[:count]
        i += 1
    return res


strs = ["flower", "florida","floff"]
res = longestCommonPrefix(strs)
print(res)