def fib(n):
                c[0] += 1
                if n > 1:
                                return fib(n-1) + fib(n-2)
                else:
                                return 1
for i in range(10):
                c = [0]
                fib(i)
                print(c[0])