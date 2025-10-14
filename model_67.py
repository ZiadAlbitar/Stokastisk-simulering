from gillespie import SSA
import numpy as np
import matplotlib.pyplot as plt

N = 1000
I0 = 5
S0 = N - I0 
E0 = 0
D0 = 0
R0 = 0
V1_0 = 0
V2_0 = 0
IM0 = 0

t0 = 0
t1 = 120
tspan = (0, 120)

# Coeffiecients
B = 0.3
ALFA = 0.4 
MU = 0.01  
GAMMA = 1/7 
VAC1 = 8.8
VAC2 = 2.45
VAC2_R = 0.05
SIGMA1 = 0.98 
SIGMA2 = 0.95
THETA = 0.2 
OMEGA1 = 0.03
OMEGA2 = 0.01


X0 = [S0, E0, I0, D0, R0, V1_0, V2_0, IM0]

def stoch():
    return np.array([[-1,1,0,0,0,0,0,0], #S -> E
                     [0,-1,1,0,0,0,0,0], #E -> I
                     [0,0,-1,1,0,0,0,0], #I -> D
                     [0,0,-1,0,1,0,0,0], #I -> R
                     [-1,0,0,0,0,1,0,0], #S -> V1
                     [0,0,0,0,-1,1,0,0], #R -> V1
                     [0,0,0,0,0,-1,0,1], #V1 -> IM
                     [0,0,0,0,0,-1,1,0], #V1 -> V2
                     [0,0,0,0,0,0,-1,1],  #V2 -> IM
                     [0,1,0,0,0,-1,0,0], #V1 -> E
                     [0,1,0,0,0,0,-1,0], #V2 -> E
                     [0,0,0,0,-1,0,1,0] #R -> V2
                     ]) 

def propp(X, coeff):
    B = coeff[0]
    ALFA = coeff[1]
    MU = coeff[2]
    GAMMA = coeff[3]
    VAC1 = coeff[4]
    VAC2 = coeff[5]
    VAC2_R = coeff[6]
    SIGMA1 = coeff[7]
    SIGMA2 = coeff[8]
    THETA = coeff[9]
    OMEGA1 = coeff[10]
    OMEGA2 = coeff[11]

    S = X[0]
    E = X[1]
    I = X[2]
    D = X[3]
    R = X[4]
    V1 = X[5]
    V2 = X[6]
    IM = X[7]

    if (R == 0):
        VAC2_R = 0

    if (V1 == 0):
        SIGMA1 = 0
    
    if (V2 == 0):
        SIGMA2 = 0
    
    w = np.array([B * (I/N) * S,
                  ALFA * E,
                  MU * I,
                  GAMMA * I,
                  VAC1 * S/(S + R),
                  VAC1 * R/(S + R),
                  SIGMA1,
                  (VAC1/5) * THETA,
                  SIGMA2,
                  OMEGA1 * (I/N)*V1,
                  OMEGA2 * (I/N) * V2,
                  VAC2_R])
    return w


X0 = (S0, E0, I0, D0, R0, V1_0, V2_0, IM0)
coeff = (B, ALFA, MU, GAMMA, VAC1, VAC2, VAC2_R, SIGMA1, SIGMA2, THETA, OMEGA1, OMEGA2) 

t, X = SSA(propp, stoch, X0, tspan, coeff) 

plt.plot(t, X[:,0], label="S")
plt.plot(t, X[:,1], label="E")
plt.plot(t, X[:,2], label="I")
plt.plot(t, X[:,3], label="D")
plt.plot(t, X[:,4], label="R")
plt.plot(t, X[:,5], label="V1")
plt.plot(t, X[:,6], label="V2")
plt.plot(t, X[:,7], label="IM")
plt.legend()
plt.grid()
plt.show()
