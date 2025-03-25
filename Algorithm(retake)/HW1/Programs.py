import random
import time

import sys
sys.setrecursionlimit(10**6)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
    # low <= j < high
        if arr[j] <= pivot:
            i = i + 1
            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # swap arr[i+1] and arr[high]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def randomized_partition(arr, low, high):
    # randomize pivot low <= pivot < high
    rand_index = random.randint(low, high)
    # swap arr[rand_index] and arr[high]
    # swap pivot to the end to work the partition(arr, low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    return partition(arr, low, high)

def randomized_select(arr, low, high, i):
    # average-case O(n)
    # worst-case O(n^2) 
    # partition is randomized form the ch05 ppt
    # find i-th smallest element in arr[low:high]
    if low == high:
        return arr[low]
    q = randomized_partition(arr, low, high)
    k = q - low + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, low, q - 1, i)
    else:
        return randomized_select(arr, q + 1, high, i - k)

def deterministic_select(arr, i):
    # linear selection algorithm
    # if n <= 5, find answer by insertion sort and return
    if len(arr) <= 5:
        return insertion_sort(arr)[i - 1]
    
    # divide arr into groups of 5 elements
    medians = []
    for j in range(0, len(arr), 5):
        # find median in each group by insertion sort
        group = arr[j:j+5]  
        # the empty part is filled with empty elements
        # use the lower median if the group has even number of elements
        medians.append(insertion_sort(group)[(len(group) - 1) // 2])  
    
    # find median of medians
    median_of_medians = deterministic_select(medians, (len(medians) + 1) // 2)
    
    # partition arr into left, mid, and right
    # mid is the elements equal to median_of_medians 
    # mid is needed to cheek the same elements as median_of_medians in arr
    left = [x for x in arr if x < median_of_medians]
    mid = [x for x in arr if x == median_of_medians]
    right = [x for x in arr if x > median_of_medians]
    
    # act same as randomized_select()    
    # but do not use randomized_partition()
    if i <= len(left):
        # i-th smallest element is in left
        return deterministic_select(left, i)
    elif i <= len(left) + len(mid):
        # i-th smallest element is Median
        return median_of_medians
    else:
        # i-th smallest element is in right
        # which is (i - len(left) - len(mid))-th smallest element in right
        return deterministic_select(right, i - len(left) - len(mid))

def insertion_sort(arr):
    # insertion sort for small array
    for i in range(1, len(arr)):
        for j in range(i, 0, -1): 
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

def checker(arr, i, result):
    # check if the result is the i-th smallest element
    # need to act in O(n) time
    # problem: if there are same elements in arr
    smaller = 0
    equal = 0
    for j in range(len(arr)):
        if arr[j] < result:
            smaller += 1
        if arr[j] == result:
            equal += 1
    return smaller < i <= smaller + equal
    
def main():
    # (1) Read all input data into memory.
    arr = [random.randint(1, 50000000000000) for _ in range(1000002)]
    i = 50  # Example selection
    
    # (2) Run the randomized-select algorithm for the given input, and measure the time.
    # Print the i-th smallest number and the time.
    
    # randomized_select() running time
    start = time.time()
    r_select_result = randomized_select(arr[:], 0, len(arr) - 1, i)
    r_time = time.time() - start
    
    # (3) Check the correctness of your randomized-select implementation by a checker pro-
    # gram. Print the result of checking. The checker program gets the input (n elements
    # and i) and the output (the i-th smallest number your program returns) as its input
    # and checks whether the output is correct or not. The checker program for selection
    # should run in linear time.
    print(f"Randomized-Select {i}-th smallest: {r_select_result}, Time: {r_time:.6f}s")
    print(f"Checker Result: {checker(arr, i, r_select_result)}")
    
    # (4) Run the deterministic-select algorithm for the given input, and measure the time.
    # Print the i-th smallest number and the time.
    
    # deterministic_select() running time
    start = time.time()
    d_select_result = deterministic_select(arr[:], i)
    d_time = time.time() - start
    
    # (5) Check the correctness of your deterministic-select implementation. Print the result
    # of checking.
    print(f"Deterministic-Select {i}-th smallest: {d_select_result}, Time: {d_time:.6f}s")
    print(f"Checker Result: {checker(arr, i, d_select_result)}")
    

    
        
if __name__ == "__main__":
    main()
