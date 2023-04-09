import matplotlib.pyplot as plt
import numpy as np
ReducedTemperature = [1.0, 1.1, 1.2, 1.3, 1.5, 2.0]
RMV = list(np.arange(0, 7, 0.1))
# RT 값에 따른 RP 값 구함.
def GetReducedPressure(RMV):
    ReducedPressure = [] # RP = Reduced Pressure 
    for x in RMV :
        temp = 8*t/(3*x-1)-(3/x*x)
        ReducedPressure.append(temp)
    return ReducedPressure

# getGraph
for t in ReducedTemperature:
    name = 'Pr-Vr Graph : ' + str(t)
    plt.plot(RMV, GetReducedPressure(RMV), label = name)

plt.legend()
plt.show()
