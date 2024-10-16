import numpy as np
import quadrature as qd

def f_1(x):
    return np.sqrt(1 + np.cos(x)**2)



def f_2(x):
    return np.sin(x)/x

a = 0
b = np.pi


n = 3000
result_thirds_1 = qd.simpsonsthird(f_1, a, b, n)
print('For function a')
print(f"Approximate integral using Simpson's 1/3: {result_thirds_1}")
result_eights_1 = qd.Simpsonseights(a, b, f_1, n)
print(f"Approximate integral using Simpson's 3/8: {result_eights_1}" '\n')


a = 1
b = 2
n = 3000

result_thirds_2 = qd.simpsonsthird(f_2, a, b, n)

print('For function b')
print(f"Approximate integral using Simpson's 1/3: {result_thirds_2}")
result_eights_2 = qd.Simpsonseights(a, b, f_2, n)

print(f"Approximate integral using Simpson's 3/8: {result_eights_2}")