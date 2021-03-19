def mySqrt(x: int) -> int:
    res = 0
    if x == 1:
        return 1
    else:
        for i in range(int(x / 2) + 1):
            if i*i <= x:
                res = i
            else:
                break
    return res

a = mySqrt(4)
print(a)