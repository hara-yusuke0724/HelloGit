import sympy as sym
def Fib(n):
    if n==1:
        return 0
    else:
        A = sym.Matrix([
            [1,1],
            [1,0]
        ])
        FibArray=A**(n-2)
        return FibArray[0,0]

#試しに計算してみる
print([Fib(n) for n in range(1,10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21