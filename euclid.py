a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

def euclidean_algorithm(a, b):
    r = a % b
    while (r > 0):
        a,b = b,r
        r = a % b
    return (b)

print(euclidean_algorithm(a, b))

def are_comprime(a, b):
    r = a % b
    while (r > 0):
        a,b = b,r
        r = a % b
    if (r == 1):
        return (True)
    return (False)

if (are_comprime(a, b)):
    print("aとbは互いに素である")
else:
    print("aとbは互いに素でない")

# r = a % b

# while (r > 0):
#     a,b = b,r
#     r = a % b

# print(b)
