import matplotlib.pyplot as plt
import numpy as np

'''
이분법으로 환원 몰랄 부피 구하기
'''
import random

# f(x) = ax^3 + bx^2 + cx + d = 0골이라고 하자.
def getRMV(Pr, Tr):
    a = 1
    b = ((Pr+8*Tr)/(3*Pr)) * (-1)
    c = 3/Pr
    d = -(1/Pr)
    print(a, b, c, d)
    def f(x):
        return (a * x**3) + (b * (x**2)) + (c * x) + d

    while True:
        r1 = random.randint(-100, 100)
        r2 = random.randint(-100, 100)
        if f(r1) * f(r2) < 0:
            p = r1
            q = r2
            break

    m = p + (q-p)/2
    err = abs(f(m))
    n = 0
    while err > 10**(-4):
        n = n + 1
        if (f(m) * f(p)) < 0 :
            q = m
        else :
            p = m
        m = p + (q-p)/2
        err = abs(f(m))

    return m

# Z 값 구하기
def Z(x, Tr):
    count_term = 100
    estimated = 1 + (((1/3) - (9/8/Tr)))/x
    square_val = 1/3/x

    for n in range(2, count_term):
        estimated += square_val**(n)
    return estimated

# 그래프 그리기
Pr = list(np.arange(0.1, 7, 0.1))
Zlist = []
TrList = [1.0, 1.1, 1.2, 1.3, 1.5, 2.0]
for j in TrList :
    for i in Pr:
        Vr = getRMV(i, j)
        # print(Vr)
        Zlist.append(Z(Vr, j))
    name = 'Z-Pr Graph' + str(j)
    plt.plot(Pr, Zlist, label = name)
    Zlist = []

plt.xlabel('Reduced Pressure')
plt.ylabel('Z')
plt.xlim([0.0, 7.0])
plt.ylim([0.0, 1.5])
plt.legend()
plt.show()

