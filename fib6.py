def fibonacci(n, a=1, b=0):
    return b if n < 1 else fibonacci(n - 1, a + b, a)

[fibonacci(i) for i in range(10)]