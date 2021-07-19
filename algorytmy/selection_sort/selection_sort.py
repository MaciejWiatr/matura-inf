def find_smallest_index(arr):
    smallest = arr[0]  # Zmienna przechowująca najmniejszą wartość
    smallest_index = 0  # Zmienna przechowująca indeks najmniejszej wartości

    for i in range(len(arr)):  # Dla każdego elementu w tablicy
        if arr[i] < smallest:  # Sprawdzam czy jest mniejszy niż smallest
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selecton_sort(arr):
    sortedArr = []
    for i in range(len(arr)):  # Dla każdego elementu w tablicy
        print(i)
        smallest_index = find_smallest_index(arr)  # Znajduję indeks najmniejszej liczby
        smallest = arr.pop(smallest_index)  # Wybieram najmniejszy element i go usuwam
        sortedArr.append(smallest)  # Dodaje najmniejszy element do nowej tablicy
    return sortedArr


print(selecton_sort([5, 3, 6, 2, 10]))
