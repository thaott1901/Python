
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        length = len(str(x))
        mid = length // 2 + length % 2
        first_half = int(x / 10**(length - mid))
        print(length)
        print(mid)
        print(first_half)
        second_half = 0
        x_copy = x
        for i in range(mid):
            print("------------------------")
            second_half = second_half * 10
            print(second_half)
            second_half = second_half + x_copy % 10
            print(second_half)
            x_copy = int(x_copy / 10)
            print(x_copy)
        if first_half == second_half:
            return True
        else:
            return False


x = 12321
a = isPalindrome(x)
print(a)
