import linearsys as ls

#Original System:
A = [   [0, 0, 0, -1, 4, 2, 0, 0, 0 ,0],
        [0, 0, 0, 0, 0, 0, 0, -1, 4, 2],
        [0, -1, -1, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 5, 2, 0, 0],
        [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1, 4],
        [0, 0, 0, 0, 0, 0, -1, 4, 2, 0],
        [-1, 4, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 4, 2, 0, 0, 0, 0, 0]    
    ]
b = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]

def partial_pivot(A, b):
    n = len(A)
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
    return A, b

partial_pivot(A, b)
print(f"Sorted Matrix:\n{ls.np.matrix(A)}\n")   #hash to hide sorted matrix
sol, niter, relerr = ls.JacobiSolve(A, b, ls.np.ones(10), 1e-15, 1000)
print("Solution:")
for n in range(10):
    print(f"\tx{n+1} = {sol[n]}")
print(f"Number of Iterations: {niter}")
print(f"Relative Error: {relerr}\n")