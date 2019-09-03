def fib(n):
    val, prev = 1, 1
    for _ in range(n-1):
        val, prev = val + prev, val
    else:  
        return val
fib(100) #>>> 573147844013817084101