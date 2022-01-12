file = open("./dane/mniejsza_na_lewo.txt", "r")
lines = file.readlines()

nums = [int(x) for x in lines[1].strip().split(" ")]

w = [-1] * len(nums)

for i in range(nums):
    for j in range(i):
        if nums[j] < nums[i]:
            w[i] = max(w[i], nums[j])

print(*w, end='')
