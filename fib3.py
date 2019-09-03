# -*- coding: utf-8 -*-
def fib(n):
                c[0] += 1
                if n > 1:
                                return fib(n-1) + fib(n-2)
                else:
                                return 1
c = [0]
print(fib(4))
print("fib(n)の呼び出し回数:{}".format(c[0]))