from rootpoly import *
import numpy as np
import matplotlib.pyplot as plt

def max_function_value(p, roots):
    max_value = np.linalg.norm([abs(horner(p, root)[0]) for root in roots], np.inf)
    return max_value

for n in [20, 40, 50]:

  # Generate the polynomial for n
  p = []
  for k in range(1, n+1):
    p.append(k**k % 7)
  
  # Find the roots using the Newton-Horner method
  eps = np.finfo(float).eps
  roots = newtonhorner(p, complex(1,1), 100, 1e3*eps, 100, 1e-3, True)[0]

  # Generate plots
  plt.style.use('seaborn-v0_8-whitegrid')
  plt.figure()
  plt.title(f"Roots for n = {n}")
  plt.plot(roots.real, roots.imag, ".")
  plt.show()

  # print(f"Roots for n={n}:", roots)
  
  # Calculate for the Maximum Function Value
  max_func_val = max_function_value(p, roots)
  print(f"Maximum function value of approximate roots for n = {n}: {max_func_val:.10e}")