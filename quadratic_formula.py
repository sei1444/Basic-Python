a,b,c = map(int, input("a b cの値: ").split())

x1 = (-b + (b**2 - 4 * a * c)**(1 / 2)) / (2 * a)
x2 = (-b - (b**2 - 4 * a * c)**(1 / 2)) / (2 * a)

print(x1, x2)
