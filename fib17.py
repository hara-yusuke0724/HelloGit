# -*- coding: utf-8 -*-
from collections import deque
def fib(n):
                stack_n = list()  # 最初の折り返しまでのnを収納するスタック。
                d = deque(maxlen=2)  # fib(n)の値を収納するキュー。
                while n > 1:
                                n -= 1
                                stack_n.append(n)  # 行きのnの値を取得。
                else:  # n = 1のとき
                                p = 1  # fib(1)の戻り値1をpに取得。
                                d.append(1)  # fib(0)の値をキューに取得。
                                d.append(p)  # fib(1)の値をキューに取得。
                while stack_n:  # 1,2,3,,,がstack_n.pop()で得られる。
                                n = stack_n.pop()  # 1回目の再帰の帰りのnを取り出す。
                                n -= 1  # 2回目の再帰
                                q = d.popleft()  # qの左側からf(n)の戻り値を取得。
                                p += q  # fib(n+2)の値を取得。
                                d.append(p)  # fib(n+2)の値をキューに取得。
                return d.pop()  # キューの右側の値を取得。
print(fib(40))