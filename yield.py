def g():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
i = g()

def fib(n):
    return [next(i) for _ in range(n)]
    
print(fib(100))