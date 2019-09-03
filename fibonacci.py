import numpy as np
def fib(n):
    A = np.matrix([[0, 1],
                   [1, 1]], dtype=np.int64)
    R = np.matrix([[0],
                   [1]], dtype=np.int64)
    
    R = A ** (n - 1) * R
    
    return R[1, 0]
for i in range(1, 5):
    print('{:,}'.format(fib(i)))