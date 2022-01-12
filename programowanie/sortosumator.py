from functools import cmp_to_key

file = open("./dane/suma_cyfr_ksHfWZp.txt", "r")
lines = [x.strip() for x in file.readlines()]
file.close()


def getDigitSum(number):
    sum = 0
    for n in number:
        sum += int(n)
    return sum


def suma_cyfr(x):
    suma = 0
    for s in x:
        suma += int(s)
    return (suma, int(x))


def cmp(i, j):
    return getDigitSum(i) - getDigitSum(j)


lines.sort(key=suma_cyfr)

print(lines, end=" ")
