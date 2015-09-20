import math

def ctg(x):
    return 1/math.tan(x)

def f(x):
    return ctg(1.05*x) - x*x

def df(x):
    return -2*x - 1.05 / math.sin(1.05 * x) ** 2

def secant(f, a, b):
    return (a * f(b) - b * f(a)) / (f(b) - f(a))

def newton(f, dumb, x):
    return x - f(x)/df(x)

def combined(f, a, b):
    x = newton(f, a, b)
    return secant(f, x, b)

def solve(func, epsilon, a = 0, b = 0, iteration = 0, method = newton):
    x = method(func, a, b)
    while abs(x-b) > epsilon:
        b = x
        iteration += 1
        x = method(func, a, b)
    return x, iteration

print("secant")
print(solve(func = f, epsilon = 0.0000000001, a = -2.95, b = -2.8, method = secant))
print("newton")
print(solve(func = f, epsilon = 0.0000000001, b = -2.8, method = newton))
print("combined")
print(solve(func = f, epsilon = 0.0000000001, a = -2.95, b = -2.8, method = combined))

def f1(x):
    return math.sin(x + 0.5) - 1

def g1(y):
    return -math.cos(y - 2)