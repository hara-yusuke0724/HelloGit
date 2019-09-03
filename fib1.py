def fib(m):
        result = []
        a = 1
        b = 1
        while a < m:
                result.append(a)
                a, b = b, a+b
        return result
   
 
print(fib(1000))
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]