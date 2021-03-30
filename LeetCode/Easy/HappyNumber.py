def isHappy(self, n: int) -> bool:
    temp = 0
    count = 0
    while True:
        s = str(n)
        for i in s:
            temp += int(i) ** 2
        n = temp
        temp = 0
        count += 1
        if n == 1:
            break
        if count > 10:
            break
    return n == 1