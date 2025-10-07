from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
B = 0.3
Y = 1/7
N = 1000.0
I0 = 5.0
S0 = N - I0
R0 = 0.0
v0 = np.array([S0, I0, R0])
tt = np.arange(0, 120, 0.1)
t0 = 0
t1 = 120
tspan = (t0, t1)


def S_prim(t, v):
    S, I, R = v
    return -(B * I / N) * S 

def I_prim(t, v):
    S, I, R = v
    return (B * I/N) * S - Y * I 

def R_prim(t, v):
    S, I, R = v
    return Y * I 

def I(t):
    return 1000 - S(t) - R(t)

def R(t):
    return 1000 - I(t) - S(t)

def S(t):
    return 1000 - I(t) - R(t)

def ode_rhs(t, v):
    return np.array([S_prim(t, v), I_prim(t, v), R_prim(t, v)])

sol = solve_ivp(ode_rhs, tspan, v0, t_eval=tt) 
    
plt.plot(sol.t, sol.y[0], label="S(t)")
plt.plot(sol.t, sol.y[1], label="I(t)")
plt.plot(sol.t, sol.y[2], label="R(t)")
plt.grid()
plt.legend()
plt.show()

