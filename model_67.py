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
C0 = I0 # Cases, to count total infected

t0 = 0
t1 = 120
tspan = (0, 120)

# Coeffiecients
B = 0.3 
ALFA = 0.3 
MU = 0.01  
GAMMA = 1/7 
VAC1 = 4 * 2
VAC2 = 0.04 * 2
VAC2_R = 0.01 * 2
SIGMA1 = 1 
SIGMA2 = 1.3
OMEGA1 = 0.03
OMEGA2 = 0.01


X0 = [S0, E0, I0, D0, R0, V1_0, V2_0, IM0, C0]

def stoch():
    return np.array([[-1,1,0,0,0,0,0,0,0], #S -> E
                     [0,-1,1,0,0,0,0,0,1], #E -> I
                     [0,0,-1,1,0,0,0,0,0], #I -> D
                     [0,0,-1,0,1,0,0,0,0], #I -> R
                     [-1,0,0,0,0,1,0,0,0], #S -> V1
                     [0,0,0,0,-1,1,0,0,0], #R -> V1
                     [0,0,0,0,0,-1,0,1,0], #V1 -> IM
                     [0,0,0,0,0,-1,1,0,0], #V1 -> V2
                     [0,0,0,0,0,0,-1,1,0], #V2 -> IM
                     [0,1,0,0,0,-1,0,0,0], #V1 -> E
                     [0,1,0,0,0,0,-1,0,0], #V2 -> E
                     [0,0,0,0,-1,0,1,0,0]  #R -> V2
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
    OMEGA1 = coeff[9]
    OMEGA2 = coeff[10]

    S = X[0]
    E = X[1]
    I = X[2]
    D = X[3]
    R = X[4]
    V1 = X[5]
    V2 = X[6]
    IM = X[7]

    # Make sure nothings becomes negative
    if (R == 0):
        VAC2_R = 0

    if (V1 == 0):
        SIGMA1 = 0
    
    if (V2 == 0):
        SIGMA2 = 0
    
    w = np.array([B * (I/N) * S,             #S -> E   
                  ALFA * E,                  #E -> I
                  MU * I,                    #I -> D
                  GAMMA * I,                 #I -> R
                  VAC1 * S/(S + R),          #S -> V1
                  VAC1 * R/(S + R),          #R -> V1
                  SIGMA1,                    #V1 -> IM
                  V1 * VAC2,                 #V1 -> V2
                  SIGMA2,                    #V2 -> IM
                  OMEGA1 * (I/N)*V1,         #V1 -> E
                  OMEGA2 * (I/N) * V2,       #V2 -> E
                  VAC2_R])                   #R -> V2
    return w


X0 = (S0, E0, I0, D0, R0, V1_0, V2_0, IM0, C0)
coeff = (B, ALFA, MU, GAMMA, VAC1, VAC2, VAC2_R, SIGMA1, SIGMA2, OMEGA1, OMEGA2) 
t, X = SSA(propp, stoch, X0, tspan, coeff) 

plt.plot(t, X[:,0], label="S")
plt.plot(t, X[:,1], label="E")
plt.plot(t, X[:,2], label="I")
plt.plot(t, X[:,3], label="D")
plt.plot(t, X[:,4], label="R")
plt.plot(t, X[:,5], label="V1")
plt.plot(t, X[:,6], label="V2")
plt.plot(t, X[:,7], label="IM")
plt.plot(t, X[:,8], label="C")
plt.legend()
plt.grid()
plt.show()
