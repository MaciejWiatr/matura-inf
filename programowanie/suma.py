k = 0
przedzial = []

with open("./dane/suma.txt", "r") as f:
    tekst = f.readlines()
    k = tekst[0].strip()
    przedzial = tekst[1].strip().split(" ")

print(k, przedzial)

sum = 0
for x in przedzial:
    num = int(x)
