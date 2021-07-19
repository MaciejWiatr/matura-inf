def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def recursive_binary_search(arr, low, high, item):
    if high >= low:
        mid = low + (high - 1) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            return recursive_binary_search(arr, low, mid-1, item)
        else:
            return recursive_binary_search(arr, mid+1, high, item)
    else:
        return -1


arr = [1, 2, 3, 4, 5]
print(recursive_binary_search(arr, 0, len(arr)-1, 4))
# print(sum([1, 2, 3, 4, 5]))
# print(max([1, 2, 3, 4, 5, 6, 7]))
