items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(list, item):
    low = 0  # Pierwszy element tabeli
    high = len(list) - 1  # Ostatni element tabeli

    while low <= high:  # Dopóki nie pozostanie jeden element
        mid = (low + high) // 2  # Wybieramy środkowy element
        guess = list[mid]  # Wybieramy środkowy element tabeli
        if guess == item:  # Znaleziono element
            return mid
        if guess > item:  # Guess był większy niż poszukiwana liczba
            high = mid - 1
        elif guess < item:  # Guess był mniejszy niż poszukiwana liczba
            low = mid + 1
    return None  # Nie znaleziono


print(binary_search(items, 8))


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
