def quicksort(arr):
    if len(arr) < 2:  # Przypadek podstawowy
        return arr
    else:
        pivot = arr[0]
        lesser = [el for el in arr[1:] if el <= pivot]
        greater = [el for el in arr[1:] if el > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
