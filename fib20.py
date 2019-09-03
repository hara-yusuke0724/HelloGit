def fib(n):
                lst = [1, 1]
                for i in range(1, n-1):
                                lst = lst[1], sum(lst)
                return sum(lst)
print(fib(40))