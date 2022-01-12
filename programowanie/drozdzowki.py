file = open("./dane/drozdzowki.txt", "r")
lines = file.readlines()
data = lines[0]
file.close()


for idx, val in enumerate(data.strip().split(" ")):
    if int(val) <= 50000:
        print(f"{idx+1};{val}")
        break
