file = open("./dane/rower.txt", "r")
line = file.readlines()[0]
dane = [int(x) for x in line.strip().split(" ")]

sum = 0
for i in range(1, len(dane), 2):
    sum += dane[i]

print(sum)
