from turtle import color
from mpmath import iv
import numpy as np
from intervals import iterate, compute_state_x1, compute_state_x2
from integrator import solve_ode
import matplotlib.pyplot as plt

X1 = iv.mpf([1,1.1])
X2 = iv.mpf([0,0])
U = iv.mpf([0,0])
dt = 0.001
steps = 1000
w  = 5

X1_hist, X2_hist = [X1], [X2]

for i in range(steps):
    I1, I2 = iv.mpf([-1,1]), iv.mpf([-1,1])
    T = iv.mpf([0,dt])
    I1, I2 = iterate(I1, I2, X1, X2, T, w, U)
    X1 = compute_state_x1(X1, X2, U, I1, dt, w)
    X2 = compute_state_x2(X1, X2, U, I2, dt, w)
    X1_hist.append(X1)
    X2_hist.append(X2)
    print(X2)
y_mins = [float(x.a) for x in X1_hist]
y_maxs = [float(x.b) for x in X1_hist]
time = np.linspace(0, dt*len(X1_hist), len(X1_hist))

plt.plot(time, y_mins, color="blue")
plt.plot(time, y_maxs, color="blue")
for x0 in np.linspace(1, 1.1, 10):
    for u0 in np.linspace(0, 0, 10):
        sol = solve_ode(w, u0, time, [x0, 0])
        sol_x1 = sol[:, 0]
        plt.plot(time, sol_x1, color="red")
plt.show()
print(X1_hist)

