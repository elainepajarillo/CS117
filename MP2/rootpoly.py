import numpy as np

def horner(p,z):
    lenp = len(p)
    b = np.zeros_like(p,dtype=complex)
    b[-1] = p[-1]
    for k in range(lenp-2,-1,-1):
      b[k] = p[k] + b[k+1]*z
    return [b[0],b[range(1,lenp)]]

def newtonhorner(p, z, maxit, tol, refmax, reftol, ref = False):
    
    def newton_raphson(p, z, maxit, tol):
      eps = np.finfo(float).eps
      err = tol + 1
      for k in range(maxit): # While k < maxit
        zold = z
        pz, df = horner(p, z)
        qk = horner(df, z)[0]
        if abs(qk) > eps:
          z = z - (pz / qk)
          err = max(abs(z - zold), abs(pz))
        else:
          err = 0
          print("Division by a small number.")
        if err < tol:
          return [z, k, err]
        elif err > tol and k >= maxit:
          raise RuntimeError("Maximum iterations exceeded.")
      return [z, k, err]

    n = len(p) - 1
    zn = np.zeros(n, dtype=complex)
    eps = np.finfo(float).eps
    pnm = [p]
    for m in range(n):
      z = complex(z, z)
      if m == n - 1:
        z = -pnm[m][0] / pnm[m][1]
      else:
        z = newton_raphson(pnm[m], z,  maxit, tol)[0]
      if ref:
        z = newton_raphson(p, z, refmax, reftol * tol)[0]
      zn[m] = z
      pnm.append(horner(pnm[m],z)[1])
    return [zn, pnm]
