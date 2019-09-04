def fibonacci_new(n): 
    a = 0
    b = 1
    for i in range(0, n): 
        a, b = b, a + b

    return a
  
# Driver Program 
  
# print(Fibonacci(9)) 
  