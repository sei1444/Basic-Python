import math
from math import sin

a = 0
b = math.pi / 2
N = 100

h = (b - a) / N
S = 0
for k in range(1, N + 1):
    S += sin(a + (k - 1) * h) + sin(a + k * h)
S *= h / 2

print(S)
