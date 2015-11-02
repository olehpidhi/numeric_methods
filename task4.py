from matplotlib import pyplot as plt
import numpy as npy


def f(x):
    return x * x * npy.cos(x + 1)

a = 0
b = 2.0
N = 20
h = (b - a) / N

xF = []
yF = []
for i in range(N + 1):
    xF.append(a + i * h)
    yF.append(f(xF[i]))


def trapezes(accuracy):
    n = N
    r = h
    count = 0
    while r ** 2 > accuracy:
        r /= 2
        n *= 2
        count += 1
    result = (r / 2) * (f(a) + f(b))
    for i in range(1, n):
        result += r * f(a + r * i)
    return result, count, n


def rectangles(accuracy):
    result = 0
    n = N
    r = h
    count = 0
    while r ** 2 > accuracy:
        r /= 2
        n *= 2
        count += 1
    for i in range(n):
        result += r * f(a + (i + 1 / 2) * r)
    return result, count, n


def simpson(accuracy):
    n = N
    r = h
    count = 0
    while r ** 4 > accuracy:
        r /= 2
        n *= 2
        count += 1
    result = f(a) + f(b) + 4 * f(a + r / 2)
    for i in range(1, n):
        result += 2 * f(a + i * r) + 4 * f(a + (i + 1 / 2) * r)
    result *= r/ 6
    return result, count, n


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

epsilon = 0.0000000001

print("Rect")
print(rectangles(epsilon))
print("Trap")
print(trapezes(epsilon))
print("Simpson")
print(simpson(epsilon))
print("Gauss4")
print(gauss4())
print("Gauss5")
print(gauss5())
plt.plot(xF, yF)
plt.show()