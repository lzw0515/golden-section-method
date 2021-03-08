# data: 2021/3/8

import math

def f_x(x):
    return math.e**(-x)+x**2

a = 0
b = 1
a1=a+(b-a)*0.382
b1=b-(b-a)*0.382

while((b-a) > 0.2):
    if f_x(a1) > f_x(b1) :
        a = a1
        a1 = b1
        b1 = round( (b - (b-a)*0.382), 3)
    else:
        b = b1
        b1 = a1
        a1 = round( (a + (b-a)*0.382), 3)
    #print(a,b)

x = round( ((b+a)/2), 3)
min = round( f_x(x) ,3)
print("求得的极值点为：",x,"求得的极值为：",min)