from gillespie import SSA
import numpy as np
import matplotlib.pyplot as plt
B = 0.2
gamma = 1/7
alfa = 0.4 # DET HÄR VI SKA SKOLLA
N = 1000.0
I0 = 5.0
S0 = N - I0
E0 = 0.0
R0 = 0.0
v0 = np.array([S0, E0, I0, R0])
t0 = 0
t1 = 120
tspan = (t0, t1)

# reaktion 1: en blir smittad och blir inkubation [-1, 1, 0, 0]
# reaktion 2: en exponerad blir smittande [0, -1, 1, 0]
# reaktion 3: en smittad blir resistant [0, 0, -1, 1]
def stochSEIR():
    M = np.array([[-1, 1, 0, 0],
                  [0, -1, 1, 0],
                  [0, 0, -1, 1]])
    return M


# X = [S, E, I, R]
# reaktion 1: en blir smittad och blir inkubation beta*(I/N)*s
# reaktion 2: en exponerad blir smittande alpha*E
# reaktion 3: en smittad blir resistant gamma*I
def propSEIR(X, coeff):
    beta=coeff[0]
    alpha=coeff[1]
    gamma=coeff[2]
    w = np.array([beta*X[2]*X[0]/N, alpha*X[1], gamma*X[2]])
    return w


X0 = (S0, E0, I0, R0)
coeff= (B, alfa, gamma)

tests = 4

plt.figure(figsize=(tests*5, 5))
for i in range(tests):
    t, X = SSA(propSEIR, stochSEIR, X0, tspan, coeff)
    a = plt.subplot(1, tests, i + 1)
    plt.plot(t, X[:,0], label="S")
    plt.plot(t, X[:,1], label="E")
    plt.plot(t, X[:,2], label="I")
    plt.plot(t, X[:,3], label="R")
    plt.grid()  
    plt.legend()    


plt.show()



