def groupAnagrams(strs):
    dict = {}
    for s in strs:
        key = tuple(sorted(s))
        dict[key] = dict.get(key, []) + [s]
    return dict.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
print(res)
