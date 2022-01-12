with open("./dane/kolorowe_nawiasy.txt", "r") as f:
    lines = f.readlines()[1::]
    res = 0
    for line in lines:
        stos = []
        for letter in map(lambda x: int(x), line.split(" ")):
            if letter > 0:
                stos.append(letter)
            elif len(stos) > 0 and stos[-1] == abs(letter):
                stos.pop()
        if len(stos) == 0:
            res += 1
    print(res)
