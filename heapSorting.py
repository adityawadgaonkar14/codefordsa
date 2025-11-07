def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # left child
    right = 2 * i + 2  # right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)


# ---- Main Program ----
arr = list(map(int, input("Enter numbers separated by space: ").split()))

print("Original array:", arr)
heap_sort(arr)
print("Sorted array in ascending order:", arr)








Algorithm: Heap Sort
1.	Start
2.	Input the array of n elements.
3.	Build a max heap from the array
(Make sure each parent node is greater than its children.)
4.	Repeat the following steps until the heap size becomes 1:
o	Swap the first element (maximum) with the last element.
o	Reduce the heap size by 1.
o	Heapify the root element to maintain the max heap property.
5.	The array is now sorted in ascending order.
6.	Stop

