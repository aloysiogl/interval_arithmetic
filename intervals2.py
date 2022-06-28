from this import d
from time import time
from mpmath import iv

# print(iv.mpf([-1,1])**2)
# print(iv.mpf([-1,1])-iv.mpf([0,1]))

def compute_interval_x1(X1, X2, T):
    """
    Computes the interval range for the piccard iterate of x1
    """
    B = X2

    return X1 + B*T

def compute_interval_x2(X1, X2, T, w, U):
    """
    Computes the interval range for the piccard iterate of x2
    """

    B = -X1*(w**2) + U
    
    return X2 + B*T

# w = 5
# factor = 1
# T = iv.mpf([0,0.1])
# X1 = iv.mpf([-1,1])
# X2 = iv.mpf([-1,1])
# I1, I2 = iv.mpf([-1,1])*factor, iv.mpf([-1,1])
# U = iv.mpf([-1,1])

def iterate(X1, X2, T, w, U):
    """
    Computes an iterate to reduce interval bounds
    """
    def step():
        X1_n = compute_interval_x1(X1, X2, T)
        X2_n = compute_interval_x2(X1, X2, T, w, U)
        return X1_n, X2_n
    X1_n, X2_n = step()
    # Expand intervals
    while not X1_n in X1 or not X2_n in X2:
        X1, X2 = X1_n, X2_n
        X1_n, X2_n = step()
        X1, X2 = X1*2, X2*2

    for _ in range(100):
        if not X1_n in X1 or not X2_n in X2:
            break
        X1, X2 = X1_n, X2_n
        X1_n, X2_n = step()
        # print("Iter")
    return X1, X2

# I1, I2 = iterate(X1, X2, T, w, U)
# print(I1, I2)

def compute_state_x1(X1, X2, U, I1, t, w):
    return X1+X2*t+1/2*(U-(w**2)*I1)*t**2

def compute_state_x2(X1, X2, U, I2, t, w):
    return X2+(U-(w**2)*X1)*t-1/2*((w**2)*I2)*t**2

# print(compute_state_x1(X1, X2, U, I1, T, w))
# print(compute_state_x2(X1, X2, U, I2, T, w))

