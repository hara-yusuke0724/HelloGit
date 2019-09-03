def t(n):
                if n == 0:
                                return 0
                elif n == 1:
                                return 2
                else:
                                return t(n-1) + t(n-2)
def T(n):
                if n > 0:
                                return T(n-1) + t(n-1)
                else:
                                return 1
print(T(9))