import sys


def binary_search(arr):
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        # Left half will be always smaller than index
        if arr[middle] < middle:
            left = middle + 1
        # Right half will be always bigger than index
        elif arr[middle] > middle:
            right = middle - 1
        # index and element matches
        else:
            return middle
    return -1


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(binary_search(arr))
