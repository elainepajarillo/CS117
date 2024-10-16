from rootscalar import newton_raphson, printf

f = lambda x : x**6 - 576  # Derived f(x)
df = lambda x: 6*(x**5)    # f'(x)

exact = 2**(1/2) * 3**(1/3) * 4**(1/4)
approx = newton_raphson(f, df, 3, 10, 1e-9, 0.5, 0.5)

printf("Real Value", exact, 9)
printf("Approximate Value", approx[0], 9)
printf("Iterations", approx[1], 0)
printf("Error", approx[2], 9)