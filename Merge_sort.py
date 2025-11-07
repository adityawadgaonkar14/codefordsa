def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Divide into left half
        right_half = arr[mid:]  # Divide into right half

        # Recursive call to sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  # i for left_half, j for right_half, k for main array

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# -------- MAIN PROGRAM --------
n = int(input("Enter number of online orders: "))
orders = []

for i in range(n):
    time = int(input(f"Enter estimated delivery time for order {i+1} (in minutes): "))
    orders.append(time)

print("\nOriginal delivery times:", orders)

merge_sort(orders)

print("Sorted delivery times (Quickest first):", orders)


Algorithm: Sort Online Orders by Delivery Time using Merge Sort
1.	Start
2.	Input the list of delivery times.
3.	If the list has more than one element:
a. Divide the list into two halves — left and right.
b. Recursively apply Merge Sort on both halves.
c. Merge the two sorted halves into a single sorted list (smallest first).
4.	Output the sorted delivery times (quicker deliveries first).
5.	Stop

