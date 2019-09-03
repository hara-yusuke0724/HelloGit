def fib(m):
        if n <= 2:
                return 1
        else:
                return fib(n-1) + fib(n-2)
               
                
result = []

for n in range(1,20):
        result.append(fib(n))


print(result)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]