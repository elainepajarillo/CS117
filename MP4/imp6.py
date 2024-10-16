from odescalar import runge_kuttta3, runge_kuttta4
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y - (1/x) * y**2

if __name__ == '__main__':
    t0 = 1  # Initial time
    tk = 1.2  # Final time
    y0 = 1  # Initial condition
    h = 0.001  # Step size

    # Solve the ODE using Runge-Kutta Method of order three (RKH3)
    t_values_rkh3, y_values_rkh3 = runge_kuttta3(f, y0, t0, tk, h)

    # Find the approximate value of y(1.2) using RKH3
    index_rkh3 = int((tk - t0) / h)
    y_approx_rkh3 = y_values_rkh3[index_rkh3]
    print(f"Approximate value of y(1.2) using RKH3: {y_approx_rkh3}")

  
    # Solve the ODE using Runge-Kutta Method of order four (RK4)
    t_values_rk4, y_values_rk4 = runge_kuttta4(f, y0, t0, tk, h)

    # Find the approximate value of y(1.2) using RK4
    index_rk4 = int((tk - t0) / h)
    y_approx_rk4 = y_values_rk4[index_rk4]
    print(f"Approximate value of y(1.2) using RK4: {y_approx_rk4}")