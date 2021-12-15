# Bajtek lubi i gwiazdki, i plusiki. Jest ciekawy, które z nich wygenerują mu większą liczbę. Na wejściu (dane w pliku tekstowym) Bajtek dostaje 5 par liczb całkowitych. Jego zadaniem jest wypisanie dla każdej z par - maksimum z pierwszego elementu w parze zwiększonego o 10 oraz z drugiego elementu podniesionego do potęgi drugiej. Pomóż Bajtkowi z tym zadaniem, i wypisz maksima dla każdej linii oddzielone średnikiem.

# Przykład danych wejściowych:
# 1 2
# 3 4
# 5 6
# 7 8
# 9 10

with open("./dane/gwiazdki.txt") as f:
    for line in f:
        a, b = line.split()
        a = int(a)
        b = int(b)
        print(a + 10, b ** 2, sep=" ")
