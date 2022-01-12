file = open("./dane/zad25_dane.txt", "r")
lines = file.readlines()
file.close()

# fibonacci


# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1

#     return fib(n-1) + fib(n-2)


# for i in range(20):
#     print(fib(i), end=", ")

fib20 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
         144, 233, 377, 610, 987, 1597, 2584, 4181, ]

# 1 Podaj ile jest liczb w pliku, które są zawarte w ciągu Fibonacciego.
nums = [int(x) for x in lines]

common = 0
for n in nums:
    if n in fib20:
        common += 1

print(f"Wspólne {common}")

elem_ciagu = []
for n in nums:
    if n in fib20:
        elem_ciagu.append(n)

print(sorted(elem_ciagu)[-1])

sum_parzystych = 0
for i in elem_ciagu:
    if i % 2 == 0:
        sum_parzystych += i

print(f"Suma parzystych {sum_parzystych}")

for i in fib20[:5]:
    if i in elem_ciagu:
        print(i, end=" ")
