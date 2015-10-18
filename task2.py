import numpy as npy
import matplotlib.pyplot as plt
import numpy.linalg as linalg


def f(x):
    return x * x * npy.cos(x + 1)
N = 20
a = 0
b = 2.0
h = (b - a) / N
finite_differences = []
data = []
factorials = []
xValues = []

data.append(f(a))
xValues.append(a)
factorials.append(1)
for i in xrange(1, N + 1):
    data.append(f(a + i * h))
    xValues.append(a + i * h)
    factorials.append(factorials[i-1] * i)

finite_differences.append(data)

for i in xrange(1, len(data)):
    finite_differences.append([])
    for j in xrange(0, len(finite_differences[i - 1]) - 1):
        finite_differences[i].append(finite_differences[i-1][j+1] - finite_differences[i-1][j])


def forward_newton(x):

    accumulator = f(a)
    t = (x - a) / h
    numerator = 1
    for i in xrange(1, N + 1):
        numerator *= t
        accumulator += finite_differences[i][0] * numerator / factorials[i]
        t -= 1
    return accumulator

newton = []
newtonX = []

h1 = (b - a) / 30
for i in xrange(0, 31):
    newtonX.append(a + i * h1)
    newton.append(forward_newton(a + i * h1))

n = N // 2


def forward_gauss(x):
    t = (x - (b-a) / 2.) / h
    accumulator = finite_differences[0][n]
    numeratorOdd = t
    numeratorEven = t * (t-1)
    i = 1
    while i <= n:
        accumulator += (finite_differences[2 * i - 1][n - i + 1] * numeratorOdd) / factorials[i * 2 - 1]
        accumulator += (finite_differences[2 * i][n - i] * numeratorEven) / factorials[i * 2]
        numeratorEven *= (t + i - 1) * (t - i + 1)
        numeratorOdd *= (t + i - 1) * (t - i)
        i += 1
    return accumulator

gauss = []
gaussX = []

for i in xrange(0, 21):
    gaussX.append(a + i * h)
    gauss.append(forward_gauss(a + i * h))


plt.plot(xValues, data)
plt.plot(newtonX, newton)
plt.plot(gaussX, gauss)


# TASK 3. Least squares method
def phi(x,i):
    return x**i;


def scalar_phi(i, j):
    result = 0
    for k in range(N + 1):
        result += phi(xValues[k], i) * phi(xValues[k], j)
    return result


def scalar(i):
    result = 0
    for k in range(N + 1):
        result += f(xValues[k]) * phi(xValues[k], i)
    return result

matrix = []
for i in range(N + 1):
    matrix.append([])
    for j in range(N + 1):
        matrix[i].append(scalar_phi(i, j))
b = []
for i in range(N + 1):
    b.append(scalar(i))

solution = linalg.solve(matrix, b)


def F(x):
    result = 0
    for i in xrange(N + 1):
        result += solution[i] * phi(x,i)
    return result

FValues = []

for i in xrange(N+1):
    FValues.append(F(xValues[i]))


def Norm(func):
    result = 0
    for i in range(N):
        result += (func(xValues[i + 1]) ** 2 + func(xValues[i]) ** 2) * (xValues[i + 1] - xValues[i]) / 2.
    return npy.sqrt(result)

print(abs(Norm(f) - Norm(F)))
plt.plot(xValues, FValues)
plt.show()
