def reverse(x: int):
    # result = 0
    # num = abs(x)
    # while num > 0:
    #     result = (result * 10) + (num % 10)
    #     num = int(num / 10)
    # if -(2**31) < (-1 * result) and x < 0:
    #     return -1 * result
    # elif (2**31 - 1) > result and x > 0:
    #     return result
    # else:
    #     return 0
    sign = -1
    if x >= 0:
        sign = 1
    numstr = str(abs(x))
    numstr = numstr[::-1]
    rev = int(numstr)
    if -(2 ** 31) <= (sign * rev) and (sign * rev) <= (2 ** 31 - 1):
        return sign * rev
    else:
        return 0