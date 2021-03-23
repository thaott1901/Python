def myAtoi(self, s: str) -> int:
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sign = ['-', '+']
    res = ''
    s1 = s.strip().split(' ')
    for i, value in enumerate(s1[0]):
        if (i == 0 and s1[0][i] in sign) or value in nums:
            res += value
        else:
            break
    try:
        if int(res) <= -2 ** 31:
            return -2 ** 31
        elif int(res) >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return int(res)
    except ValueError:
        return 0
