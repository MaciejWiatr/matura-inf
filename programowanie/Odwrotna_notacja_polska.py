operation = []
stos = []

f = open("./dane/odwrotna.txt", "r")
operation = f.readline().replace("x", "*").strip().split(" ")
f.close()

znaki = "*+-/"

for x in operation:
    if x not in znaki:
        stos.append(int(x))
    else:
        first = stos.pop()
        second = stos.pop()
        nums = sorted([first, second], reverse=True)
        print(f"{nums[0]}{x}{nums[1]}")
        stos.append(eval(f"{nums[0]}{x}{nums[1]}"))

print(stos[0])
