import math

n = float(input("nの値を入力: "))

def isPrime(n):
    if isinstance(n, float):
        raise ValueError("nは整数である必要があります")
    if (n <= 0):
        raise ValueError("nは自然数である必要があります")
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return True

if isPrime(n):
    print("nは素数でない")
else:
    print("nは素数である")

"""
n = int(input("nの値を入力: "))

a = 0
for i in range(2, int(math.sqrt(n) + 1)):
    if (n % i == 0):
        a = 1
        break

if (a):
    print("nは素数でない")
else:
    print("nは素数である")
"""