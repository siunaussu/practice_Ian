from ast import List


def muilt_jc(n: int) -> int:
    """阶乘"""
    if n < 0:
        return 0

    if n <= 1:
        return 1

    res = n * muilt_jc(n - 1)

    return res

# print(muilt_jc(10))


from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)

def fibonacci_list(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_list(n - 1) + fibonacci_list(n - 2)

# print(fibonacci_list(10))

def bubble_sort(arr):
    """
    Sorts a list in ascending order using the bubble sort algorithm.
    Modifies the list in-place and returns it.
    """
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swap happened in this pass
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

    return arr

# print(bubble_sort(a))

def bubble_my(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

a = [2,3,1,4,123,4,2,6,7,89,-1,0,1]
print(bubble_my(a))
