import matplotlib.pyplot as plt
import numpy as np

RMV = np.arange(0.5, 1, 0.1) # RMV = Reduced Molar Volume
ReducedTemperature = [1.0, 1.1, 1.2, 1.3, 1.5, 2.0] # RT = Reduced Temperature

# RT 값에 따른 RP 값 구함.
def GetReducedPressure():
    ReducedPressure = [] # RP = Reduced Pressure 
    for t in ReducedTemperature :
        for x in RMV :
            temp = 8*t/(3*x-1)-(3/x*x)
            ReducedPressure.append(temp)
    ReducedPressure.sort()
    return ReducedPressure

Rp = GetReducedPressure()

# test
x = list(np.arange(0.5, 10, 0.1))
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

for i in x:
    tmp1 = float(1/(1-(1/3*(i**(-1)))))
    tmp2 = float(9/(8*1.0*i))
    tmp = tmp1 - tmp2
    y1.append(tmp)
plt.plot(x, y1, label = 'Z (Reduced Temperature = 1.0)')

for i in x:
    tmp1 = float(1/(1-(1/3*(i**(-1)))))
    tmp2 = float(9/(8*1.1*i))
    tmp = tmp1 - tmp2
    y2.append(tmp)
plt.plot(x, y2, label = 'Z (Reduced Temperature = 1.1)')

for i in x:
    tmp1 = float(1/(1-(1/3*(i**(-1)))))
    tmp2 = float(9/(8*1.2*i))
    tmp = tmp1 - tmp2
    y3.append(tmp)
plt.plot(x, y3, label = 'Z (Reduced Temperature = 1.2)')

for i in x:
    tmp1 = float(1/(1-(1/3*(i**(-1)))))
    tmp2 = float(9/(8*1.3*i))
    tmp = tmp1 - tmp2
    y4.append(tmp)
plt.plot(x, y4, label = 'Z (Reduced Temperature = 1.3)')

for i in x:
    tmp1 = float(1/(1-(1/3*(i**(-1)))))
    tmp2 = float(9/(8*1.5*i))
    tmp = tmp1 - tmp2
    y5.append(tmp)
plt.plot(x, y5, label = 'Z (Reduced Temperature = 1.5)')

for i in x:
    tmp1 = float(1/(1-(1/3*(i**(-1)))))
    tmp2 = float(9/(8*2.0*i))
    tmp = tmp1 - tmp2
    y6.append(tmp)
plt.plot(x, y6, label = 'Z (Reduced Temperature = 2.0)')

plt.legend()
plt.show()
