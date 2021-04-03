
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    res = 1
    if n <= 2:
        return res
    else:
        res = fib(n -1) + fib(n -2)
        memo[n] = res
    return res

x = fib(10)
print(x)
print(memo)
