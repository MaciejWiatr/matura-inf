a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))

delta = (b**2) - (4*a*c)

root1 = (-b + delta**0.5)/(2*a)
root2 = (-b - delta**0.5)/(2*a)

print(round(root1, 2), round(root2, 2), sep="; ")
