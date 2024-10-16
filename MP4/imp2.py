import numpy as np
import matplotlib.pyplot as plt
from polyinterp import NewtonLagrangeInterpolation

def f(x):
    return x / (1 - x**2 + x**4)**2

def compute_norm(f, pn, start, end, norm_type='2'):
    x_values = np.linspace(start, end, 9000)
    difference = f(x_values) - pn(x_values)
    return np.linalg.norm(difference, ord=float(norm_type))  # Convert norm_type to float

# Plotting
start, end = -2, 2
n_values = [5, 10, 20]

# Create subplots
fig, axs = plt.subplots(1, len(n_values), figsize=(15, 5))

for i, n in enumerate(n_values):
    # Generate equidistant nodes
    nodes = np.linspace(start, end, n+1)

    # Create interpolation function using Newton-Lagrange method
    interpolation_function = NewtonLagrangeInterpolation(f, nodes)

    # Plot f(x) and pn for each n
    x_values = np.linspace(start, end, 1000)
    axs[i].plot(x_values, f(x_values), label='f(x)')
    axs[i].plot(x_values, interpolation_function(x_values), label=f'p{n}(x)')
    axs[i].set_title(f'n = {n}')
    axs[i].legend()
    
    # Plot the nodes
    axs[i].plot(nodes, f(nodes), "ro")

    # Add grid and labels
    axs[i].grid(True)
    axs[i].set_xlabel('x')  # Fix the function name to set_xlabel
    axs[i].set_ylabel('y')  # Fix the function name to set_ylabel

    # Compute and print the norms
    norm_inf = compute_norm(f, interpolation_function, start, end, np.inf)
    print(f"For n = {n}: ||f - p{n}||_∞ = {norm_inf}")

plt.show()