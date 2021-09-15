# NWD - Największy wspólny dzielnik
def NWD(pierwsza: int, druga: int):
    if pierwsza == druga:
        return pierwsza

    if pierwsza > druga:
        pierwsza = pierwsza - druga
    if pierwsza < druga:
        druga = druga - pierwsza

    return NWD(pierwsza, druga)


# print(NWD(42, 112))
print(100000 // 3212)
print(100000 % 3211)
