import sympy as sym
def Fib(n):
    x = sym.symbols('x',nonnegative=True,integer=True) #変数xの宣言(非負の整数)
    Fib=1/sym.sqrt(5)*(((1+sym.sqrt(5))/2)**(n-1)-((1-sym.sqrt(5))/2)**(n-1)) #一般項の式
    result=Fib.subs(x,n) #xにnを代入
    result=result.evalf() #式を浮動小数点数として評価
    return int(result)
Fiblist=[]
for n in range(1,10):
    Fiblist+=[Fib(n)]
print(Fiblist)
# [0, 1, 1, 2, 3, 5, 8, 13, 21]