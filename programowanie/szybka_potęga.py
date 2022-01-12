def potega(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            x = potega(a, n//2)
            return x*x
        else:
            return a * potega(a, n - 1)


print(potega(3, 10))
