B = ""
A = "--./..-/..---/"

for i in A.split("/"):
    for j in i:
        if j == "-":
            B += right(j)
        elif j == ".":
            B += left(j)

# Musze do tego wrócić
