from gekko import GEKKO
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

### Code for this project was written by Brent M. Lund ###

for num in range(1, 10):               #This is Amdahl's Law
    variable = 1 / num                  #variable represents the percentage change for the equation or fraction enhanced
    variable1 = (1 - variable)          # 1 - by the fraction enhanced
    variable2 = (variable / num)        #fraction enhanced / number of core processors
    variable3 = variable1 + variable2   #Variable1 was added to variable2
    variable4 = 1 / variable3           #divided one by the final product of variable 3
    print("Processor cores Added: ", num)
    print("Final Point of Amdel's Law: ", variable4)

result = [1, 1.3333, 1.28, 1.23, 1.19, 1.16, 1.13, 1.12]
plt.plot(result)
plt.show()

print("An Amdel Law derivative: ")
def Amdel_Law_derivative(derivative):                                       #derivitave of Amdel's_Law
    k = .03
    derivative_V = derivative * (derivative + 1)                            #multiplied fraction enhanced with-
    derivative_X = (derivative - (derivative - 1 *(k)))                   #the number of core processors
    derivative_Y = (derivative_X) * (derivative_X)                          #the number of core processors-
    derivative_Z = derivative_V / derivative_Y
                                                                           #subtracted it by fraction enhanced
                                                                          #multiplied this result by itself
    print(derivative_Z)

Amdel_Law_derivative(1)
Amdel_Law_derivative(2)
Amdel_Law_derivative(3)
Amdel_Law_derivative(4)
Amdel_Law_derivative(5)
Amdel_Law_derivative(6)
Amdel_Law_derivative(7)
Amdel_Law_derivative(8)

# function that returns dy/dt
def model(y, t):                            #applied my derivative of Amdel's_Law above-
                                            #and plugged it into the model function
        dev_v = y * (y + 1)
        dev_x = (y - (y - 1 * (.03)))
        dev_y = (dev_x) * (dev_x)
        dev_z = dev_v / dev_y
        dydt = dev_z
        return dydt

# initial condition
y0 = 1

# time points
t = np.linspace(0, 1000)  # shows my eleven points between 0 and 10

y = odeint(model, y0, t)

# plot results
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
















