# for Many Inputs, Use
# sys.stdin.readLine().rstrip()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        else:
            return 'yes'
    return 'no'


n = int(input())
inventory = list(map(int, input().split()))

m = int(input())
order = list(map(int, input().split()))
inventory.sort()

# using binary search
for no in order:
    print(binary_search(inventory,no,0,n-1),end=' ')
print()

# using counting sort
count_array = [0 for i in range(1000001)]
for i in inventory:
    count_array[i]=1
for no in order:
    if count_array[no]:
        print('yes',end=' ')
    else:
        print('no',end=' ')
print()


# using set
tree = set(inventory)
for no in order:
    if no in tree:
        print('yes',end=' ')
    else:
        print('no',end=' ')
print()