from gillespie import SSA
import numpy as np
import matplotlib.pyplot as plt

X0 = [995, 5, 0]

N = 1000
beta = 0.3
gamma = 1/7
tspan = (0, 120)

def prop(X, coeff):
    #beta * I / N  * S
    prop0 = coeff[0]*(X[1] / N) * X[0] # 1.4925
    #gamma * I
    prop1 = coeff[1] * X[1] #
    return np.array([prop0, prop1])

# reaktion 1: En mottaglig blir sjuk
# reaktion 2: En mottaglig blir resistant
def stoch():
    return np.array([[-1, 1, 0],
                     [0, -1, 1]])


coeff = (beta, gamma)

t, X = SSA(prop, stoch, X0, tspan, coeff)
t, X = SSA(prop, stoch, X0, tspan, coeff)
t, X = SSA(prop, stoch, X0, tspan, coeff)
t, X = SSA(prop, stoch, X0, tspan, coeff)
t, X = SSA(prop, stoch, X0, tspan, coeff)


plt.plot(t, X[:,0], label="S")
plt.plot(t, X[:,1], label="I")
plt.plot(t, X[:,2], label="R")
plt.legend()
plt.grid()
plt.show()
