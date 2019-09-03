from collections import deque
def fib(n):
                d = deque(maxlen=2)
                p = 1
                d.append(1)
                d.append(p)
                while n > 1:
                                n -= 1
                                q = d.popleft()
                                p += q
                                d.append(p)
                return d.pop()  
print(fib(40))