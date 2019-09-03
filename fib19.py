from collections import deque
def fib(n):
                d = deque([1, 1], maxlen=2)
                p = 1
                while n > 1:
                                n -= 1
                                q = d.popleft()
                                p += q
                                d.append(p)
                return d.pop()
print(fib(40))