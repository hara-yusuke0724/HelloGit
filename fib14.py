def fib(n):
                stack_n = list()
                while n > 1:
                                n -= 1
                                stack_n.append(n)
                else:
                                p = 1
                while stack_n:
                                n = stack_n.pop()
                                n -= 1
                                if not n > 1:
                                                q = 1
                                else:
                                                q = fib(n)
                                p += q
                return p
print(fib(7))