from rootscalar import *

f = lambda x : (np.exp(np.cos(x)) - 3*(np.sin(x)))
g = lambda x : np.arcsin(np.exp(np.cos(x)) / 3)
df = lambda x : -np.exp(np.cos(x)) * np.sin(x) - 3 * np.cos(x)

results = {
  "Newton-Raphson": newton_raphson(f, df, 0, 1000, 1e-10, 0.5, 0.5),
  "(Forward) Newton-Raphson": newton_raphson_inexact(f, 1, 0, 1000, 1e-10, 0.5, 0.5),
  "(Backward) Newton-Raphson": newton_raphson_inexact(f, 2, 0, 1000, 1e-10, 0.5, 0.5),
  "(Central) Newton-Raphson": newton_raphson_inexact(f, 3, 0, 1000, 1e-10, 0.5, 0.5),
  "Steffensen": steffensen(f, 0, 1000, 1e-10, 0.5, 0.5),
  "Picard Fix Point": fixpoint(g, 0, 1000, 1e-10),
}

header = {
  "Method" : 27,
  "Root x" : 28,
  "Iteration k" : 14,
  "Error" : 25,
  "Function Value f(x)" : 22,
}

for string, length in header.items():
  printff(string, length)
print("")

for method, result in results.items():
  print(f"{method:<27} {result[0]:<+28.15e} {result[1]:<14} {result[2]:<+25.15e} {f(result[0]):<+22.15e}")