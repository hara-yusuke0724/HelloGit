# -*- coding: utf-8 -*-
def fib(n):
                stack_n = list()  # 最初の折り返しまでのnを収納するスタック。
                list_m = list()  # fib(n)の値を収納するリスト。nは要素番号に一致。
                while n > 1:  # CONDITION_A
                                n -= 1  # CODE_B
                                stack_n.append(n)  # 行きのnの値を取得。
                else:  # n = 1のとき
                                p = 1  # fib(1)の戻り値1をpに取得。CODE_D
                                list_m.append(p)  # fib(0)の値をスタックに取得。(上図の通りだとf(1))  再帰の結果をリストに保存しておく。
                                list_m.append(1)  # fib(1)の値をスタックに取得。(上図の通りだとf(0))
                while stack_n:  # 1,2,3,,,がstack_n.pop()で得られる。
                                n = stack_n.pop()  # 1回目の再帰の帰りのnを取り出す。
                                n -= 1  # 2回目の再帰のCODE_B
                                q = list_m[n]
                                p += q  # fib(n+2)の値を取得。
                                list_m.append(p)  # fib(n+2)の値をスタックに取得。
                return list_m[-1]
print(fib(40))