from matplotlib import pyplot as plt
import numpy as npy


def f(x):
    return x * x * npy.cos(x + 1)

N = 20
a = 0
b = 2.0
h = (b - a) / N

xF = []
yF = []
for i in range(N + 1):
    xF.append(a + i * h)
    yF.append(f(xF[i]))


def trapezes(accuracy, N):
    n = N
    n1 = n * 2
    r = (b-a)/n
    r1 = r/2
    result = (r / 2) * (f(a) + f(b))

    for i in range(1, n):
        result += r * f(a + r * i)
    result1 = (r1 / 2) * (f(a) + f(b))
    for i in range(1, n1):
        result1 += r1 * f(a + r1 * i)
    if npy.abs((result - result1)/(2 ** 2 - 1)) > accuracy:
        return trapezes(accuracy, N * 2)
    return result


def rectangles(accuracy, N):
    result = 0
    result1 = 0
    n = N
    r = (b-a)/n
    n1 = 2*N
    r1 = (b-a)/n1
    for i in range(n):
        result += r * f(a + (i + 1 / 2) * r)
    for i in range(n1):
        result1 += r1 * f(a + (i + 1 / 2) * r1)
    if npy.abs((result - result1)/(2 ** 2 - 1)) > accuracy:
        return rectangles(accuracy, N * 2)
    return result


def simpson(accuracy, N):
    n = N
    n1 = 2*n
    r = (b-a)/n
    r1 = r/2
    result = f(a) + f(b) + 4 * f(a + r / 2)
    for i in range(1, n):
        result += 2 * f(a + i * r) + 4 * f(a + (i + 1 / 2) * r)
    result *= r / 6

    result1 = f(a) + f(b) + 4 * f(a + r / 2)
    for i in range(1, n1):
        result1 += 2 * f(a + i * r1) + 4 * f(a + (i + 1 / 2) * r1)
    result1 *= r1 / 6
    if npy.abs((result - result1)/(2 ** 4 - 1)) > accuracy:
        return simpson(accuracy, N * 2)
    return result


def gauss4():
    t1 = t4 = 0.861136
    t2 = t3 = 0.339981
    t4 *= -1
    t3 *= -1
    c1 = c4 = 0.347855
    c2 = c3 = 0.652145
    result = c1 * f((b + a) / 2 + (b - a) * t1 / 2) + c2 * f((b + a) / 2 + (b - a) * t2 / 2)
    result += c3 * f((b + a) / 2 + (b - a) * t3 / 2) + c4 * f((b + a) / 2 + (b - a) * t4 / 2)
    result *= (b - a) / 2
    return result


def gauss5():
    t1 = t5 = 0.90618
    t2 = t4 = 0.538469
    t3 = 0
    t5 *= -1
    t4 *= -1
    c1 = c5 = 0.23693
    c2 = c4 = 0.47863
    c3 = 0.56889
    result = c1 * f((b + a) / 2 + (b - a) * t1 / 2) + c2 * f((b + a) / 2 + (b - a) * t2 / 2)
    result += c3 * f((b + a) / 2 + (b - a) * t3 / 2) + c4 * f((b + a) / 2 + (b - a) * t4 / 2)
    result += c5 * f((b + a) / 2 + (b - a) * t5 / 2)
    result *= (b - a) / 2
    return result

epsilon = 0.00001

print("Rect")
print(rectangles(epsilon, N))
print("Trap")
print(trapezes(epsilon, N))
print("Simpson")
print(simpson(epsilon, N))
print("Gauss4")
print(gauss4())
print("Gauss5")
print(gauss5())
plt.plot(xF, yF)
plt.show()