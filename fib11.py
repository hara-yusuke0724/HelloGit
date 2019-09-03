def t(n):
                if n == 0:
                                return 0
                elif n == 1:
                                return 2
                else:
                                return t(n-1) + t(n-2)