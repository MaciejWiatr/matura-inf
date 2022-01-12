file = open("./dane/gielda.txt", "r")
lines = file.readlines()
wyniki = lines[0]
liczby = [int(x) for x in wyniki.strip().split(" ")]

kupIdx = 0
sprzIdx = 0
zysk = 0

for kup in range(len(liczby)):
    for sprzed in range(kup, len(liczby)):
        if liczby[sprzed] - liczby[kup] > zysk:
            kupIdx = kup
            sprzIdx = sprzed
            zysk = liczby[sprzed] - liczby[kup]

print(f"{kupIdx+1};{sprzIdx+1};{zysk*100000};")
