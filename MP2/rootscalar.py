import numpy as np

def newton_raphson(f, fprime, x, maxit, tol, wa=0.5, wf=0.5):
    err = tol + 1
    k = 0
    while err > tol and k < maxit:
        xold = x
        x = x - f(x) / fprime(x)
        err = wa * abs(x - xold) + wf * abs(f(x))
        k += 1
    if err > tol and k == maxit:
        raise RuntimeError("Error in maximum iterate and/or tolerance")
    return [x, k, err]

def newton_raphson_inexact(f, i, x, maxit, tol, wa, wf):
  err = tol + 1 # To ensure that err > tol
  h = np.sqrt(np.finfo(float).eps)
  
  # The parameter i specifies which variant of Inexact Newton-Raphson method to use.
  if i == 1:
    qk = lambda x : (f(x+h) - f(x)) / h # Forward
  elif i == 2:
    qk = lambda x : (f(x) - f(x-h)) / h # Backward
  elif i == 3:
    qk = lambda x : (f(x+h) - f(x-h)) / (2*h) # Center
  
  for k in range(maxit): # While k < maxit
    xold = x
    x = x - ( f(x) / qk(x) )
    err = wa * abs(x - xold) + wf * abs(f(x)) 
    if err < tol:
      return [x, k+1, err]
    elif err > tol and k >= maxit:
      raise RuntimeError("Maximum iterations exceeded.")
    
def steffensen(f, x, maxit, tol, wa, wf):
  err = tol + 1 # To ensure that err > tol
  qk = lambda x : (f(x + f(x)) - f(x)) / f(x)
  for k in range(maxit): # While k < maxit
    xold = x
    x = x - (f(x) / qk(x))
    err = wa * abs(x - xold) + wf *abs(f(x))
    if err < tol:
      return [x, k+1, err]
    elif err > tol and k >= maxit:
      raise RuntimeError("Maximum iterations exceeded.")
    
def fixpoint(g, x, maxit, tol):
  err = tol + 1 # To ensure that err > tol
  for k in range(maxit): # While k < maxit
    xold = x
    x = g(x)
    err = abs(x - xold)
    if err < tol:
      return [x, k+1, err]
    elif err > tol and k >= maxit:
      raise RuntimeError("Maximum iterations exceeded.")
    
def printf(label, result, decimals):
  """ Prints a label and its result in proper desired format of specified decimals. """
  spaces = 0
  length = len(str(label))
  spaces = 20 - length
  space = " " * spaces
  print(f"{space}{label} \t {result:.{decimals}e}")

def printff(str, spaces):
  """ Prints a string with the proper number of spaces after it. """
  length = len(str)
  space = " " * (spaces - length)
  print ( '\033[1m' + f"{str}{space}" + '\033[0m', end =" ")