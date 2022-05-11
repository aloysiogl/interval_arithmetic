import numpy as np
from scipy.integrate import odeint

def ode_integrator(x, t, w, u):
    """
    Integrades spring mass system
    """

    x1, x2 = x

    x1dot = x2
    x2dot = -(w**2)*x1 + u

    return [x1dot, x2dot]


def solve_ode(w, u, t_space, x0):
    return odeint(ode_integrator, x0, t_space, args=(w, u))

# print(solve_ode(1, -1, 0.1, 0.001, [1, 1]))