import numpy as np
import matplotlib.pyplot as plt

#F0=0,F1=1を除いてn番目の数までのフィボナッチ数を計算する
print("What is the nth number?")
n = int(input())

fibo = []
a,b = 0,1
#F0,F1をリストに格納
fibo.append(a)
fibo.append(b)

for x in range(n):
    a,b = b, a+b
    fibo.append(b)
    # print(fibo)

plt.grid()
plt.plot(fibo)
plt.show()