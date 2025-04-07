import random
import time
import os
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
    # swap pivot to the end to work partition(arr, low, high)
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
    # worst-case O(n)
    # if n <= 5, find answer by insertion sort and return
    if len(arr) <= 5:
        return sorted(arr)[i - 1]  

    # Divide arr into groups of 5 elements
    # in ppt, the sorted() part is insertion sort.
    # But, I used sorted() for better time complexity
    # https://www.wild-inter.net/publications/munro-wild-2018
    medians = []
    for j in range(0, len(arr), 5):
        group = arr[j:j+5]
        # find median in each group by insertion sort
        # the empty part is filled with empty elements
        # use the lower median if the group has even number of elements
        medians.append(sorted(group)[(len(group) - 1) // 2])

    # Find the median of medians
    median_of_medians = deterministic_select(medians, (len(medians) + 1) // 2)

    # partition arr into left, mid, and right
    # mid is the elements equal to median_of_medians 
    # mid is needed to cheek the same elements as median_of_medians in arr
    left, mid, right = [], [], []
    for x in arr:
        if x < median_of_medians:
            left.append(x)
        elif x == median_of_medians:
            mid.append(x)
        else:
            right.append(x)

    # Determine which partition contains the i-th smallest element
    # due to the sudo code in the ch05 ppt use the recursive call
    if i <= len(left):
        arr = left
        return deterministic_select(arr, i)
    elif i <= len(left) + len(mid):
        return median_of_medians
    else:
        arr = right
        i -= len(left) + len(mid)
        return deterministic_select(arr, i)

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
    
def read_input(filepath):
    # read data from the input file
    with open(filepath, 'r') as f:
        arr = [int(line.strip()) for line in f]
    return arr

def generate_example_input1(filepath, n):
    """Generate an example input file with random numbers."""
    # Generate a list of random numbers between 1 and n/2
    with open(filepath, 'w') as f:
        for _ in range(n):
            f.write(f"{random.randint(1, n // 2)}\n")

def generate_example_input2(filepath, n):
    """Generate an example input file with random numbers."""
    # Generate a list of random numbers between 1 and n*2
    with open(filepath, 'w') as f:
        for _ in range(n):
            f.write(f"{random.randint(1, n * 2)}\n")

def main():
    # Prompt user for the value of n
    try:
        n = int(input("Enter the value of n (number of random numbers to generate): "))
        print(f"Received input: {n}")  # 디버깅용 출력
        
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    # Generate example input files
    print("Generating example input files...\n")
    base_dir = os.path.dirname(__file__) 

    # Filepath for generate_example_input1
    input_filepath1 = os.path.join(base_dir, "example_input1.txt")
    generate_example_input1(input_filepath1, n)
    print(f"Example input file 1 generated at: {input_filepath1}")

    # Filepath for generate_example_input2
    input_filepath2 = os.path.join(base_dir, "example_input2.txt")
    generate_example_input2(input_filepath2, n)
    print(f"Example input file 2 generated at: {input_filepath2}")
    
    # Process each example input file
    for input_filepath in [input_filepath1, input_filepath2]:
        print(f"\nProcessing file: {input_filepath}")
        
        # Ensure the input file exists
        if not os.path.exists(input_filepath):
            print(f"Input file not found: {input_filepath}")
            continue

        # (1) Read all input data into memory.
        arr = read_input(input_filepath)
        i = random.randint(1, len(arr))  # Select a random i within the range of the array
        
        # (2) Run the randomized-select algorithm for the given input, and measure the time.
        start = time.time()
        r_select_result = randomized_select(arr[:], 0, len(arr) - 1, i)
        r_time = time.time() - start
        print(f"Randomized-Select {i}-th smallest: {r_select_result}, Time: {r_time:.6f}")
        print(f"Checker Result: {checker(arr, i, r_select_result)}")
        
        # (3) Run the deterministic-select algorithm for the given input, and measure the time.
        start = time.time()
        d_select_result = deterministic_select(arr[:], i)
        d_time = time.time() - start
        print(f"Deterministic-Select {i}-th smallest: {d_select_result}, Time: {d_time:.6f}")
        print(f"Checker Result: {checker(arr, i, d_select_result)}")
    
if __name__ == "__main__":
    main()