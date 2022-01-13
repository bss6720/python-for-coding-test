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


def binary_search_iter(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        else:
            return mid
    return None


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search_recur(array, target, 0, n - 1)
print('Recursive Binary Search: ', result)

result = binary_search_iter(array, target, 0, n - 1)
print('Iterative Binary Search: ', result)
