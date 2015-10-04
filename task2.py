import numpy as npy
import matplotlib.pyplot as plt


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

plt.show()
