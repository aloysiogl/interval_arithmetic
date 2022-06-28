from turtle import color
from mpmath import iv
import numpy as np
from intervals2 import iterate, compute_state_x1, compute_state_x2
from integrator import solve_ode
import matplotlib.pyplot as plt

X1 = iv.mpf([1,1])
X2 = iv.mpf([0,0])
U = iv.mpf([0,1])
dt = 0.01
steps = 50
w  = 5

X1_hist, X2_hist = [X1], [X2]

for i in range(steps):
    T = iv.mpf([0,dt])
    I1, I2 = iterate(X1, X2, T, w, U)
    X1_n = compute_state_x1(X1, X2, U, I1, dt, w)
    X2_n = compute_state_x2(X1, X2, U, I2, dt, w)
    X1, X2 = X1_n, X2_n
    X1_hist.append(X1)
    X2_hist.append(X2)
    print((i+1)*dt)
x1_mins = [float(x.a) for x in X1_hist]
x1_maxs = [float(x.b) for x in X1_hist]
x2_mins = [float(x.a) for x in X2_hist]
x2_maxs = [float(x.b) for x in X2_hist]
time = np.linspace(0, dt*(len(X1_hist)-1), len(X1_hist))
# print(time)
# exit()

# Subpluts
fig, ax = plt.subplots(2, 1)

for x0 in np.linspace(1, 1, 10):
    for u0 in np.linspace(0, 1, 10):
        sol = solve_ode(w, u0, time, [x0, 0])
        sol_x1 = sol[:, 0]
        sol_x2 = sol[:, 1]
        ax[0].plot(time, sol_x1, color="red")
        ax[1].plot(time, sol_x2, '-', color="red")
ax[0].plot(time, x1_mins, '-', color="blue")
ax[0].plot(time, x1_maxs, '-', color="blue")
ax[0].set_title("x1")

ax[1].plot(time, x2_mins, '-', color="blue")
ax[1].plot(time, x2_maxs, '-', color="blue")
ax[1].set_title("x2")
plt.show()
print(time)

