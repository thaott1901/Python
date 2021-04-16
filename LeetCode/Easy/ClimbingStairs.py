
def climbStairsn(s: int) -> int:
    s = {}
    s[0] = 0
    s[1] = 1
    s[2] = 2
    if n <= 2:
        return n
    for i in range(3, n+1):
        s[i] = s[i-1] + s[i-2]
    return s[n]
