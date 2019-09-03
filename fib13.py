# -*- coding: utf-8 -*-
def fib(n):  # n < 6
                stack_n = list()  # 1回目の再帰呼び出しの後も使うnの値をスタックに取得。
                while n > 1:
                                n -= 1
                                stack_n.append(n)
                else:
                                p = 1  # 1回目の再帰呼び出しのf(1)の戻り値を取得。
                while stack_n:  # スタックに収納したnの値を取り出していく。
                                n = stack_n.pop()
                                n -= 1
                                if not n > 1:
                                                q = 1  # 2回目の再帰呼び出しのf(0)とf(1)の戻り値を取得。
                                else:
                                                stack_n2 = list()  # 2回目の再帰呼び出しのf(n)の引数がn>1のとき、1回目と同様にnの値をスタックに取得。
                                                while n > 1:
                                                                n -= 1
                                                                stack_n2.append(n)
                                                else:
                                                                p2 = 1
                                                while stack_n2:
                                                                n2 = stack_n2.pop()
                                                                n2 -= 1
                                                                if not n2 > 1:
                                                                                q2 = 1
                                                                else:
                                                                                pass  # n>5のときはここに繰り返しのコードを追加しないといけない。
                                                                p2 += q2
                                                                q = p2
                                                p += q
                                return p
print(fib(5))                                                              