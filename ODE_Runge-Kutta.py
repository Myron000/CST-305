from gekko import GEKKO
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = float(.1)
y = float(2)
x = float(1)

c = 3

def ODE(h, x, y):
    k1 = c*(x)*(y)              # outputs the k1 value
    print("Print: k1: ", k1)
    k2_x = (x + (h/2))            # outputs the k2 x value  1.05
    print("Print k2_x: ", k2_x)
    k2_y = (y + (h/2) *(k1))        # outputs the k2 y value  2.3
    print("Print k2_y: ", k2_y)
    k2 = c*((k2_x)*(k2_x))*(k2_y)   # outputs the k2 value:  7.60
    print("Print k2: ", k2)
    k3_x = (x + (h/2))              # output k3_x 1.05
    print("Print k3_x: ", k3_x)
    k3_y = (y +((h/2)*(k2)))          # output k3_y 2.38
    print("Print k3_y: ", k3_y)
    k3 = c*(((k3_x)*(k3_x)) *(k3_y))    # output_k3  7.87
    print("Print k3: ", k3)
    k4_x = ((x + h))                    # output k4_x 1.10
    print("Print k4_x: ", k4_x)
    k4_y = (2 + ((h*k3)))               # output k4_y
    print("Print k4_y: ", k4_y)
    k4 = c*((k4_x)*(k4_x) *k4_y)        # output k4 10.11
    print("Print k4: ", k4)

    t4 = (1/6)*((k1 + 2*(k2) + 2*(k3) + (k4)))
    print("Print t4: ", t4)                     # 7.846

    y1 = (y) + (h/6)*((k1 + 2*(k2) +2*(k3) + (k4))) # y_1 = 2.784
    print("Print y1: ", y1)

ODE(h, x, y)







