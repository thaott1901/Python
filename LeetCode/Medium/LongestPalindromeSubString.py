def longestPalindrome(s):
    size = len(s)
    res = s[0]
    for i in range(size):
        mid = i
        right = i + 1
        while mid >= 0 and right < size and s[mid] == s[right]:
            mid -= 1
            right += 1
        res = max(res, s[mid + 1:right], key=lambda x: len(x))
        left = i - 1
        right = i + 1
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
        res = max(res, s[left + 1: right], key=lambda x:len(x))
    return res


s = "ababad"
res = longestPalindrome(s)
print(res)
