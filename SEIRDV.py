from gillespie import SSA
import numpy as np
import matplotlib.pyplot as plt
B = 0.3
gamma = 1/7
alfa = 0.4 # DET HÄR VI SKA SKOLLA
mu = 0.01
v = 1
N = 1000.0
I0 = 5.0
S0 = N - I0
E0 = 0.0
R0 = 0.0
D0 = 0.0
V0 = 0.0
v0 = np.array([S0, E0, I0, R0, D0, V0])
t0 = 0
t1 = 120
tspan = (t0, t1)

# reaktion 1: en blir smittad och blir inkubation [-1, 1, 0, 0]
# reaktion 2: en exponerad blir smittande [0, -1, 1, 0]
# reaktion 3: en smittad blir resistant [0, 0, -1, 1]
def stochSEIR():
    M = np.array([[-1, 1, 0, 0, 0, 0],
                  [0, -1, 1, 0, 0, 0], 
                  [0, 0, -1, 1, 0, 0],
                  [0, 0, -1, 0, 1, 0],
                  [-1, 0, 0, 0, 0, 1]])
    return M


# X = [S, E, I, R]
# reaktion 1: en blir smittad och blir inkubation beta*(I/N)*s
# reaktion 2: en exponerad blir smittande alpha*E
# reaktion 3: en smittad blir resistant gamma*I
# reaktion 4: en smittad dör :( mu*I
# reaktion 5: en motagglig person blir vaccinerad I
def propSEIR(X, coeff):
    beta=coeff[0]
    alpha=coeff[1]
    gamma=coeff[2]
    mu=coeff[3]
    v=coeff[4]
    if (X[0] == 0):
        v = 0
    w = np.array([beta*X[2]*X[0]/N, alpha*X[1], gamma*X[2], mu*X[2], v] )
    return w


X0 = (S0, E0, I0, R0, D0, V0)
coeff= (B, alfa, gamma, mu, v)


t,X = SSA(propSEIR, stochSEIR, X0, tspan, coeff)

plt.plot(t,X[:,0], label="S")
plt.plot(t,X[:,1], label="E")
plt.plot(t,X[:,2], label="I")
plt.plot(t,X[:,3], label="R")
plt.plot(t,X[:,4], label="D")
plt.plot(t,X[:,5], label="V")
plt.legend()
plt.grid()
plt.show()



