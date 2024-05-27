import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def create_random_list(size=300, start=0, end=99):
    return [random.randint(start, end) for _ in range(size)]

def measure_sort_time(sort_func, arr, iterations=10000):
    total_time = 0
    for _ in range(iterations):
        test_arr = arr.copy()
        start_time = time.time()
        sort_func(test_arr)
        total_time += time.time() - start_time
    return total_time / iterations

sort_functions = [
    selection_sort,
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    shell_sort
]


A = create_random_list()

sort_times = {}
for sort_func in sort_functions:
    sort_times[sort_func.__name__] = measure_sort_time(sort_func, A)


print(sort_times)


sort_names = list(sort_times.keys())
sort_durations = list(sort_times.values())

plt.figure(figsize=(12, 6))
plt.bar(sort_names, sort_durations, color='skyblue')
plt.xlabel('Sort Algorithm')
plt.ylabel('Average Time (s)')
plt.title('Comparison of Sorting Algorithms')
plt.xticks(rotation=45)
plt.show()

# 병합정렬 : 머지 : 0.000277
# 퀵정렬 :  퀵 : 0.000172
# 힙정렬 : 힙 : 0.000363