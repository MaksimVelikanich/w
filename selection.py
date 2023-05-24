import random
import time

NUM = 50000

def createArray():
    random.seed(1)
    A = [random.randint(1, NUM) for _ in range(NUM)]
    B = A.copy()
    return A, B

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

totalSelectionSortTime = 0.0
totalQuickSortTime = 0.0

for _ in range(5):
    A, B = createArray()

    start_time = time.time()
    selectionSort(A)
    selection_sort_time = time.time() - start_time
    totalSelectionSortTime += selection_sort_time

    print("Selection sort time: {:.6f} sec".format(selection_sort_time))

    A = B.copy()

    start_time = time.time()
    quickSort(A, 0, NUM - 1)
    quick_sort_time = time.time() - start_time
    totalQuickSortTime += quick_sort_time

    print("Quicksort time: {:.6f} sec".format(quick_sort_time))


averageSelectionSortTime = totalSelectionSortTime / 5
averageQuickSortTime = totalQuickSortTime / 5

print("Average selection sort time: {:.6f} sec".format(averageSelectionSortTime))
print("Average quicksort time: {:.6f} sec".format(averageQuickSortTime))