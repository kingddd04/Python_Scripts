import timeit
import random

# Implementazione di QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Implementazione di MergeSort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Genera una lista casuale di numeri
size = 100000  # Numero di elementi da ordinare
arr = [random.randint(0, 10000) for _ in range(size)]

# Test con timeit
quick_time = timeit.timeit(lambda: quicksort(arr[:]), number=10)
merge_time = timeit.timeit(lambda: merge_sort(arr[:]), number=10)
py_deafult_sort_time = timeit.timeit(lambda: arr.sort(), number=10)
py_deafult_sorted_time = timeit.timeit(lambda: sorted(arr), number=10)

print(f"Tempo QuickSort: {quick_time:.5f} secondi")
print(f"Tempo MergeSort: {merge_time:.5f} secondi")
print(f"Tempo sort() nativo: {py_deafult_sort_time:.5f} secondi")
print(f"Tempo sorted() nativo: {py_deafult_sorted_time:.5f} secondi")