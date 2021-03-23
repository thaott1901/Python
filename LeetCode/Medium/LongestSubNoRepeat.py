def lengthOfLongestSubstring(self, s: str) -> int:
    sdict = {}
    start = 0
    maxcount = 0
    for i in range(len(s)):
        if s[i] in sdict and start <= sdict[s[i]]:
            start = sdict[s[i]] + 1
        else:
            maxcount = max(maxcount, i - start + 1)
        sdict[s[i]] = i
    return maxcount