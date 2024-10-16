import numpy as np
import linearsys as ls

def block(n):
    A = ls.np.zeros((n,n), dtype = float)
    a = ls.np.ones(n, dtype = float)       
    b = ls.np.array([2 if i % 2 == 0 else 1 for i in range(n)], dtype = float)                                           
    c = ls.np.array([[3,4,5][i%3] for i in range(n)])  
    d = ls.np.array([1 if i % 2 == 0 else 2 for i in range(n)], dtype = float)      
    e = ls.np.ones(n, dtype = float)                                 
    
    for i in range(n):
        A[i, i] = c[i]
        if i > 0:
            A[i, i - 1] = b[i]
            A[i - 1, i] = d[i - 1]
        if i > 1:
            A[i, i - 2] = a[i]
            A[i - 2, i] = e[i]
    return ls.np.matrix(A)

A_matrix = block(150)
print(A_matrix)


#for C
CVal = ls.np.array([[3,4,5][i%3] for i in range(150)])          # Value of C, range 150
solution1 = ls.LUSolve(block(150), CVal)                        
print("\nSolution for C:\n", solution1)

relerr_C = np.linalg.norm(CVal - np.dot(block(150), solution1)) / np.linalg.norm(CVal)      
print("Relative error for C:", relerr_C)



#for D
DVal = ls.np.array([1 if i % 2 == 0 else 2 for i in range(100)], dtype = float)         #value of D, range 100
solution2 = ls.LUSolve(block(100), DVal)
print("\nSolution for D:\n", solution2)

relerr_D = np.linalg.norm(DVal - np.dot(block(100), solution2)) / np.linalg.norm(DVal)      
print("Relative error for D:", relerr_D)
