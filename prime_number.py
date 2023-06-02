import math

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
