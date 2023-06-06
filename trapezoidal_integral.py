import math

def f1(x):
    return (math.sin(x))

def f2(x):
    return (4 / (1 + x ** 2))

def f3(x):
    return (math.sqrt(math.pi) * math.exp(-x ** 2))

def trapezoidal_integral(f, a, b, n):
    h = (b - a) / n
    S = 0
    for k in range(1, n + 1):
        S += f(a + (k - 1) * h) + f(a + k * h)
    S *= h / 2
    return S

print(trapezoidal_integral(f1, 0, math.pi / 2, 50))
print(trapezoidal_integral(f2, 0, 1, 100))
print(trapezoidal_integral(f3, -100, 100, 1000))

# a = 0
# b = math.pi / 2
# N = 100

# h = (b - a) / N
# S = 0
# for k in range(1, N + 1):
#     S += sin(a + (k - 1) * h) + sin(a + k * h)
# S *= h / 2

# print(S)