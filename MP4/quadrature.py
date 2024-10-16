import numpy as np

def Simpsonseights(a, b, f, n):
    if n % 3 != 0:
        raise ValueError("Number of subintervals must be a multiple of 3")
    h = (b - a) / n
    sum_y = 0
    sum_y_3 = 0
    yn = 0  # Initialize yn outside the loop
    for i in range(n+1):
        x = a + i * h
        y = f(x)
        if i == 0:
            y0 = y
            print("y0 = ", y0)
        elif i == n:
            yn = y
            print("yn = ", yn)
        else:
            sum_y = sum_y + y
            if (i % 3 == 0):
                sum_y_3 = sum_y_3 + y
    result = ((3 * h) / 8) * (y0 + 3 * sum_y - sum_y_3 + yn)
    return np.array(result)


def simpsonsthird(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    
    result = h / 3
    fours = 4 * sum(f(x[i]) for i in range(1, n, 2))
    twos = 2 * sum(f(x[i]) for i in range(2, n - 1, 2))
    result *= f(x[0]) + fours + twos + f(x[n])
    

    return np.array(result)