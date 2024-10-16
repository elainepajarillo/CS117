import linearsys as ls

def newton(f,Jf,x,tol,maxit):
    x = ls.np.array(x,float)
    err_newton = tol + 1
    k_newton = 0
    while err_newton > tol and k_newton < maxit:
        dx = ls.LUSolve(Jf(x),-f(x))
        x = x + dx
        err_newton = ls.np.linalg.norm(f(x))
        k_newton += 1
    if err_newton > tol and k_newton == maxit:
        print("Error in tol and / or maxit.")
    return x, err_newton, k_newton

unk = ["a*","b*","c*","d*"]
#itema
def af(x):
    x = ls.np.array(x, dtype = float)
    # a = x[0], b = x[1], c = x[2], d = x[3]
    f0 = (20 * x[0] * x[2]) - (8 * x[0] * x[1]) + (16 * x[2]**3) - (4 * x[1] * x[3]) - 39
    f1 = (12 * x[0]) + (6 * x[1]) + (2 * x[2]) - (2 * x[3]) - 11
    f2 = (4 * x[0]**2) + (2 * x[1] * x[2]) - (10 * x[2]) + (2 * x[0] * x[3]**2) + 7
    f3 = (-3 * x[0] * x[3]) - (2 * x[1]**2) + (7 * x[2] * x[3]) -16
    return ls.np.array([f0, f1, f2, f3], float)

def aJf(x):
    f00 = (20 * x[2]) - (8 * x[1])
    f01 = (-8 * x[0]) - (4 * x[3])
    f02 = (20 * x[0]) + (48 * x[2]**2)
    f03 = -4 * x[1]
    f10 = 12
    f11 = 6
    f12 = 2
    f13 = -2
    f20 = (8 * x[0]) + (2 * x[3]**2)
    f21 = 2 * x[2]
    f22 = (2 * x[1]) - 10
    f23 = 4 * x[0] * x[3]
    f30 = -3 * x[3]
    f31 = -4 * x[1]
    f32 = 7 * x[3]
    f33 = (-3 * x[0]) + (7 * x[2])
    return ls.np.array([[f00, f01, f02, f03], [f10, f11, f12, f13], [f20, f21, f22, f23], [f30, f31, f32, f33]], float)

def aA(x):
    #Function without b for the relative error
    x = ls.np.array(x, dtype = float)
    # a = x[0], b = x[1], c = x[2], d = x[3]
    f0 = (20 * x[0] * x[2]) - (8 * x[0] * x[1]) + (16 * x[2]**3) - (4 * x[1] * x[3])
    f1 = (12 * x[0]) + (6 * x[1]) + (2 * x[2]) - (2 * x[3])
    f2 = (4 * x[0]**2) + (2 * x[1] * x[2]) - (10 * x[2]) + (2 * x[0] * x[3]**2)
    f3 = (-3 * x[0] * x[3]) - (2 * x[1]**2) + (7 * x[2] * x[3])
    return ls.np.array([f0, f1, f2, f3], float)

print("Item A:")
itema = newton(af, aJf, [1,1,1,1], 1e-14, 100)
gA = ls.np.array([39, 11, -7, 16], float)   #given solution array
print(f"   Solution:")
for n in range(4):
    print(f"\t{unk[n%4]} = {itema[0][n]}")
print(f"   Error: {(ls.np.linalg.norm(aA(itema[0]) - gA))/ls.np.linalg.norm(gA)}")
print(f"   Iterations: {itema[2]}\n")

#itemb
def bf(x):
    x = ls.np.array(x, dtype = float)
    # a = x[0], b = x[1], c = x[2]
    f0 = (3 * x[0]) - ls.np.cos(x[1] * x[2]) - 0.5
    f1 = (x[0]**2) - (81 * (x[1] + 0.1)**2) + ls.np.sin(x[2]) + 1.06
    f2 = ls.np.exp(-x[0] * x[1]) + (20 * x[2]) - ((3 - (10 * ls.np.pi))/3)
    return ls.np.array([f0, f1, f2], float)

def bJf(x):
    f00 = 3
    f01 = x[2] * ls.np.sin(x[1] * x[2])
    f02 = x[1] * ls.np.sin(x[1] * x[2])
    f10 = 2 * x[0]
    f11 = -162 * (x[1] + 0.1)
    f12 = ls.np.cos(x[2])
    f20 = -x[1] * ls.np.exp(-x[0] * x[1])
    f21 = -x[0] * ls.np.exp(-x[0] * x[1])
    f22 = 20
    return ls.np.array([[f00, f01, f02], [f10, f11, f12], [f20, f21, f22]])

def bA(x):
    #Function without b for the relative error
    x = ls.np.array(x, dtype = float)
    # a = x[0], b = x[1], c = x[2]
    f0 = (3 * x[0]) - ls.np.cos(x[1] * x[2])
    f1 = (x[0]**2) - (81 * (x[1] + 0.1)**2) + ls.np.sin(x[2])
    f2 = ls.np.exp(-x[0] * x[1]) + (20 * x[2])
    return ls.np.array([f0, f1, f2], float)

print("Item B:")
itemb = newton(bf, bJf, [1,1,1], 1e-14, 100)
gB = ls.np.array([0.5, -1.06, (3 - (10 * ls.np.pi))/3], float)  #given solution array
print("   Solution:")
for n in range(3):
    print(f"\t{unk[n%4]} = {itemb[0][n]}")
gB = ls.np.array([0.5, -1.06, (3 - (10 * ls.np.pi))/3], float)
print(f"   Error: {(ls.np.linalg.norm(bA(itemb[0]) - gB))/ls.np.linalg.norm(gB)}")
print(f"   Iterations: {itemb[2]}\n")