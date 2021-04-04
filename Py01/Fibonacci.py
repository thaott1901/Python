# memo = {}

def fib(n, memo: dict):
    if n in memo:
        return memo[n]
    res = 1
    if n <= 2:
        return res
    else:
        res = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = res
    return res


d = {}
x = fib(10, d)
print(x)
print(d)
