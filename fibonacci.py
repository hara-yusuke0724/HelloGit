def fib(n):
                if n > 1:
                                n -= 1
                                p = fib(n)
                                n -= 1
                                q = fib(n)
                                m = p + q
                                return m
                else:
                                return 1
print(fib(4))