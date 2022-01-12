file = open("./dane/sport.txt", "r")
lines = file.readlines()
data = lines[0]
file.close()
data_list = data.strip().split(" ")
shoes = data_list[:1000]
balls = data_list[1000::]

sorted_shoes = [int(x) for x in sorted(shoes)]
sorted_balls = [int(x) for x in sorted(balls)]

max_val = 0

for i in sorted_shoes:
    for j in sorted_balls:
        if i + j > max_val and i + j <= 20000:
            max_val = i+j

print(max_val)
