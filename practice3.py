import matplotlib.pyplot as plt
import numpy as np
import math

# e^x 그래프 그리기
def f(x):
    count_term = 100
    estimated = 1
    square_val = x

    for n in range(1, count_term):
        current_term = 1/(math.factorial(n)) * square_val**(n)
        estimated += current_term
    return estimated

x = list(np.arange(-10, 10, 0.1))
y = []
for i in x :
    y.append(f(i))

plt.plot(x, y, label = 'e^x 그래프')
plt.legend()
plt.show()