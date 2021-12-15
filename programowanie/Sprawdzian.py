def calcGrade(p, k):
    return (p/100)**k


grades = [
    [20, 0.5],
    [31, 0.3],
    [49, 0.2],
    [89, 1.5],
]

for i in grades:
    grade = calcGrade(i[0], i[1])

    if grade > 0.4 and grade < 0.5:
        print("2", end="; ")
    elif grade >= 0.5 and grade < 0.75:
        print("3", end="; ")
    elif grade >= 0.75 and grade < 0.85:
        print("4", end="; ")
    elif grade >= 0.85 and grade < 0.95:
        print("5", end="; ")
    elif grade >= 0.95:
        print("6", end="; ")
