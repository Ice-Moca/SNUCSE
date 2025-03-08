# 12-A ppt 위한 프로그램
# sort algorithm 시간 측정임 ( 각 백번 씩)

from time import time
import random

# -------room for sort-----------

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k]=left_half[i]
                i=i+1
            else:
                arr[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            arr[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            arr[k]=right_half[j]
            j=j+1
            k=k+1
    return arr

#quick sort
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr

def q(arr):
    if len(arr)>1:
        ind=len(arr)//2
        s=[]
        l=[]
        for i,val in enumerate(arr):
            if i != ind:
                if val< arr[ind]:
                    s.append(val)
                else:
                    l.append(val)
        return q(s)+[arr[ind]]+q(l)
    else: return arr

print(q([1,2,3,4,3,2,2,3,4,5,7,6]))

#-----main--------
#그냥 빌트인 함수 sorted도 써야됨 중요!
# okay

# 일단 100개로 
total_list = 1
# total_data = 100
'''
import random

def time_measure(func, total_data, isquick=False):
    rand_list = [i for i in range(total_data)]

    time_arr = []
    for i in range(total_list):
        random.shuffle(rand_list)
        start = time()
        if isquick:
          func(rand_list,0,total_data-1)
        else:
          func(rand_list)
        end = time()
        time_arr.append(round(end - start,10))
        
        print(f"{end-start:.10f}")

print("bubble")
time_measure(bubble_sort,100)
time_measure(bubble_sort,1000)
time_measure(bubble_sort,10000)

print("selection")
time_measure(selection_sort,100)
time_measure(selection_sort,1000)
time_measure(selection_sort,10000)

print("insert")
time_measure(insertion_sort,100)
time_measure(insertion_sort,1000)
time_measure(insertion_sort,10000)

print("merge")
time_measure(merge_sort,100)
time_measure(merge_sort,1000)
time_measure(merge_sort,10000)

print("quick")
time_measure(quick_sort,100, True)
time_measure(quick_sort,1000,True)
time_measure(quick_sort,10000,True)

print("built-in")
time_measure(sorted,100)
time_measure(sorted,1000)
time_measure(sorted,10000)
'''