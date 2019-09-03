def fib(n, val=1):
    return fib(n-1, val + n) if n > 0 else val
fib(100)