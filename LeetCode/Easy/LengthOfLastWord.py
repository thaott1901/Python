def lengthOfLastWord(self, s: str) -> int:
#         rev = s[::-1]
#         start = False
#         index = -1
#         for i in range(len(rev)):
#             if not start and rev[i] != " ":
#                 start = True
#                 index = i
#         if index == -1:
#             return 0
#         for j in range(index, len(rev)):
#             if rev[j] == " ":
#                 return j - index
#         return len(rev) - index
        split = s.split()
        if not split:
            return 0
        else:
            return len(split[-1])