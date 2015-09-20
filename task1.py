import math

def ctg(x):
    return 1/math.tan(x)

def f(x):
    return ctg(1.05*x) - x*x

def df(x):
    return -2*x - 1.05 / math.sin(1.05 * x) ** 2

def secant(f, a, b):
    return (a * f(b) - b * f(a)) / (f(b) - f(a))

def newton(f, x, dumb = 0):
    return x - f(x)/df(x)

def combined(f, a, b):
    x = newton(f,a)
    return secant(f, x, b)

def solve(func, epsilon, a, b = 0, iteration = 0, method = newton):
    x = method(func, a, b)
    while abs(x-b) > epsilon:
        b = x
        iteration += 1
        x = secant(func, a, b)
    return x, iteration

print("secant")
print(solve(func = f, epsilon = 0.0000000001, a = -2.95, b = -2.8, method = secant))
print("newton")
print(solve(func = f, epsilon = 0.0000000001, a = -2.95, method = newton))
print("combined")
print(solve(func = f, epsilon = 0.0000000001, a = -2.95, b = -2.8, method = combined))

