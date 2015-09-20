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

def f2(y):
    return -math.cos(y - 2)

def solveSystem(f1, f2, x0, y0, epsilon, iteration = 0):
    xi = f1(x0)
    yi = f2(y0)
    while abs(xi - x0) > epsilon and abs(yi - y0) > epsilon:
        iteration += 1
        x0 = xi
        y0 = yi
        xi = f1(xi)
        yi = f2(yi)
    return xi, yi, iteration

print("system")
print(solveSystem(f1, f2, 0.1, -0.1, 0.000001 ))

def f1(x,y):
    return math.sin(x + 0.5) - y - 1
def df1x(x,y):
    return math.cos(x + 0.5)
def df1y(x,y):
    return -1
def f2(x,y):
    return math.cos(y-2) + x
def df2x(x,y):
    return 1
def df2y(x,y):
    return -math.sin(y-2)


def delta(x,y):
    return (df1x(x,y) * df2y(x,y) - df1y(x,y) * df2x(x,y))
def delta_x(x,y):
    return -(f1(x,y)*df2y(x,y) - df1y(x,y)*f2(x,y))
def delta_y(x,y):
    return (f1(x,y)*df2x(x,y) - df1x(x,y)*f2(x,y))

def newton_system(t, k, delta, delta_t):
    return t + delta_t(t,k)/delta(t,k)

def newton_solve(f1, f2, x0, y0, epsilon, iteration = 0):
    x = newton_system(x0,y0, delta, delta_x)
    y = newton_system(y0,x0, delta, delta_y)
    while abs(x-x0) > epsilon and abs(y-y0) > epsilon:
        iteration += 1
        x0 = x
        y0 = y
        x = newton_system(x0,y0, delta, delta_x)
        y = newton_system(x0,y0, delta, delta_y)
    return x, y, iteration

print("newton system")
print(newton_solve(f1, f2, 0.5, 0.1, 0.0000000000001))
