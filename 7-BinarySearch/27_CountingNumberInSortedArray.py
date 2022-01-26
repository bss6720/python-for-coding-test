import sys
from bisect import bisect_left, bisect_right


# Ordinary binary search
def binary_search(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < number:
            left = mid + 1
        elif arr[mid] > number:
            right = mid - 1
        else:
            return mid
    return (left + right) // 2 + 1


# binary search for first number occurrence
def first_binsearch(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return (left + right) // 2 + 1


# binary search for last number occurrence
def last_binsearch(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= number:
            left = mid + 1
        else:
            right = mid - 1
    return (left + right) // 2 + 1


# using bisect library
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# when the numbers are only integers, this can work.
l = binary_search(arr, x - 0.1)
r = binary_search(arr, x + 0.1)
print(r - l)

# first and last occurrence binary search
l = first_binsearch(arr, x)
r = last_binsearch(arr, x)
print(r - l)

# using bisect libaray
print(count_by_range(arr, x, x))
