size = int(input("Enter the array size "))
array = []

for i in range(size):
    value = int(input(f"Enter the array element {i + 1}: "))
    array.append(value)
print("Array:", array)

def insertionSort(array):
    for i in range(len(array)):
        cursor = array[i]
        pos = i
        while pos > 0 and array[pos - 1] > cursor:
            array[pos] = array[pos - 1]
            pos = pos - 1
        array[pos] = cursor
    return array

sortedArray = insertionSort(array)
print("Sorted array:", sortedArray)