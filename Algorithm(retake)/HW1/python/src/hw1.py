from typing import List
import random

def insertion_sort(arr: List[int], left: int, right: int) -> None:
    """
    Sorts a subarray using insertion sort.

    This function sorts the subarray of arr ranging from index left to right (inclusive)
    using the insertion sort algorithm.

    Parameters:
        arr (List[int]): The array containing the elements to sort.
        left (int): The starting index of the subarray.
        right (int): The ending index of the subarray.
    """
    # insertion sort for small subarray
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):
            if arr[j] < arr[j - 1]:
                # swap arr[j] and arr[j-1]
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

def randomized_select(arr: List[int], left: int, right: int, i: int) -> int:
    """
    Selects an i-th smallest element using the randomized selection algorithm.

    This function selects an i-th smallest element in the subarray arr[left...right]
    using the randomized selection algorithm.

    Parameters:
        arr (List[int]): The array containing the elements.
        left (int): The starting index of the subarray.
        right (int): The ending index of the subarray.
        i (int): The 1-based order of the element to select.

    Returns:
        int: The i-th smallest element in the specified subarray.
    """
    # average-case O(n), worst-case O(n^2)
    # partition is randomized
    if left == right:
        return arr[left]
    pivot_index = randomized_partition(arr, left, right)
    k = pivot_index - left + 1
    if i == k:
        return arr[pivot_index]
    elif i < k:
        # recursive call on the left partition
        return randomized_select(arr, left, pivot_index - 1, i)
    else:
        # recursive call on the right partition
        return randomized_select(arr, pivot_index + 1, right, i - k)

def deterministic_select(arr: List[int], left: int, right: int, i: int) -> int:
    """
    Finds an i-th smallest element using the deterministic median-of-medians algorithm.

    This function selects an i-th smallest element in the subarray arr[left...right]
    using the deterministic median-of-medians selection algorithm.

    Parameters:
        arr (List[int]): The array containing the elements.
        left (int): The starting index of the subarray.
        right (int): The ending index of the subarray.
        i (int): The 1-based order of the element to select.

    Returns:
        int: The i-th smallest element in the specified subarray.
    """
    # worst-case O(n)
    if right - left + 1 <= 5:
        # if the subarray size is <= 5, sort and return the i-th smallest
        subarray = arr[left:right + 1]
        insertion_sort(subarray, 0, len(subarray) - 1)
        return subarray[i - 1]

    # Divide arr into groups of 5 elements
    medians = []
    for j in range(left, right + 1, 5):
        group_right = min(j + 4, right)
        # sort each group using insertion sort
        insertion_sort(arr, j, group_right)
        # find the median of the groups
        medians.append(arr[j + (group_right - j) // 2])

    # Find the median of medians
    median_of_medians = deterministic_select(medians, 0, len(medians) - 1, (len(medians) + 1) // 2)

    # Partition arr using the median of medians as pivot
    pivot_index = partition_with_pivot(arr, left, right, median_of_medians)

    k = pivot_index - left + 1
    if i == k:
        return arr[pivot_index]
    elif i < k:
        # recursive call on the left partition
        return deterministic_select(arr, left, pivot_index - 1, i)
    else:
        # recursive call on the right partition
        return deterministic_select(arr, pivot_index + 1, right, i - k)

def check_selection(arr: List[int], i: int, result: int) -> bool:
    """
    Verifies the correctness of the selected element.

    This function checks in linear time whether result is indeed an i-th smallest element
    in the array.

    Parameters:
        arr (List[int]): The array containing the elements.
        i (int): The 1-based order of the element to verify.
        result (int): The element that has been selected.

    Returns:
        bool: True if result is an i-th smallest element in arr, False otherwise.
    """
    # check if the result is the i-th smallest element
    # need to act in O(n) time
    smaller = 0
    equal = 0
    for num in arr:
        if num < result:
            smaller += 1
        elif num == result:
            equal += 1
    return smaller < i <= smaller + equal

def partition(arr: List[int], low: int, high: int) -> int:
    # partition the array around the pivot
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        # low <= j < high
        if arr[j] <= pivot:
            i += 1
            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # swap arr[i+1] and arr[high]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr: List[int], low: int, high: int) -> int:
    # randomize pivot low <= pivot < high
    rand_index = random.randint(low, high)
    # swap arr[rand_index] and arr[high]
    # swap pivot to the end to work with partition(arr, low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    return partition(arr, low, high)

def partition_with_pivot(arr: List[int], low: int, high: int, pivot: int) -> int:
    # partition the array using a specific pivot
    pivot_index = arr.index(pivot, low, high + 1)
    # swap pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)
