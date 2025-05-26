def partition(arr, low, high, pivot):
    i = low - 1
    j = high + 1
    while True:
        # 왼쪽에서 pivot 이상인 요소 찾기
        i += 1
        while arr[i] < pivot:
            i += 1
        # 오른쪽에서 pivot 이하인 요소 찾기
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # 교환
        arr[i], arr[j] = arr[j], arr[i]


# 예시 사용법
arr = [33, 0, 21, 42, 59, 82, 77, 65, 91]
# arr = [77, 82, 59, 42, 21, 0, 33, 65, 91]
pivot = 91  # 원하는 pivot 값으로 변경 가능

print("Before partition:", arr)
idx = partition(arr, 1, len(arr)-1, pivot)
print("After partition:", arr)
print("Partition index:", idx)
