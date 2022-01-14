def cut_length(array, cut_height):
    count = 0
    for i in array:
        cut = i - cut_height
        count += (cut if cut > 0 else 0)
    return count


def binary_search(array, target, start, end):
    best = 0
    while start <= end:
        mid = (start + end) // 2
        current = cut_length(array, mid)
        # 잘린 떡의 길이가 target보다 낮은 경우, cut height를 줄여줘야한다.
        if target > current:
            end = mid - 1
        elif target < current:
            # 못찾는 경우 가능한 최대 cut height를 저장
            if mid > best:
                best = mid
            start = mid + 1
        else:
            return mid
    return best


n, m = map(int, input().split())
dduk = list(map(int, input().split()))

print(binary_search(dduk, m, 0, 1000000000))
