from this import d
from mpmath import iv

print(iv.mpf([-1,1])**2)
print(iv.mpf([-1,1])-iv.mpf([0,1]))

def compute_interval_x1(I1, X2, T, w):
    """
    Computes an iterate for the the interval for the state x1
    """
    B = -1/2*(T**2)*(w**2)*X2

    return (I1 + B)*T

def compute_interval_x2(I2, X1, T, w, U):
    """
    Computes an iterate for the the interval for the state x2
    """

    B = 1/2*(T**2)*(w**2)*(-U+(w**2)*X1)

    return (-(w**2)*I2+U+B)*T

w = 1
factor = 1
T = iv.mpf([0,0.1])
X1 = iv.mpf([-1,1])
X2 = iv.mpf([-1,1])
I1, I2 = iv.mpf([-1,1])*factor, iv.mpf([-1,1])
U = iv.mpf([-1,1])

def iterate(I1, I2, X1, X2, T, w, U):
    """
    Computes an iterate to reduce interval bounds
    """
    def step():
        I1_n = compute_interval_x1(I1, X2, T, w)
        I2_n = compute_interval_x2(I1, X1, T, w, U)
        return I1_n, I2_n
    I1_n, I2_n = step()
    # Expand intervals
    while not I1_n in I1 or not I2_n in I2:
        I1, I2 = I1_n, I2_n
        I1_n, I2_n = step()
        I1, I2 = I1*2, I2*2
        # print("here")

    for i in range(100):
        if not I1_n in I1 or not I2_n in I2:
            break
        I1, I2 = I1_n, I2_n
        I1_n, I2_n = step()
        # print("Iter")
    return I1, I2

I1, I2 = iterate(I1, I2, X1, X2, T, w, U)
print(I1, I2)

def compute_state_x1(X1, X2, U, I1, t, w):
    return X1+X2*t+1/2*(U-(w**2)*X1)*t**2+I1

def compute_state_x2(X1, X2, U, I2, t, w):
    return X2+(U-(w**2)*X1)*t-1/2*((w**2)*X2)*t**2+I2

print(compute_state_x1(X1, X2, U, I1, T, w))
print(compute_state_x2(X1, X2, U, I2, T, w))

