def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # Left child index
    right = 2 * i + 2  # Right child index

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root again
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


# Main program
arr = []
n = int(input("Enter the number of elements: "))
print("Enter elements:")

for i in range(n):
    num = int(input())
    arr.append(num)

print("\nOriginal Array:", arr)
heap_sort(arr)
print("Sorted Array (Ascending order):", arr)
