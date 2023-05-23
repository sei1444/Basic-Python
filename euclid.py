a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

q = a // b
r = a % b

while r > 0:
    a = b
    b = r
    q = a // b
    r = a % b

print(b)

