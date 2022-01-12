def binary_search_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] > target:
        return binary_search_recur(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search_recur(array, target, mid + 1, end)
    else:
        return mid


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search_recur(array, target, 0, n - 1)

print(result)
