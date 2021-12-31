# Programmers course 30, lessons 42891 using heapq
# Slower but, clear and easier to understand
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i))

    eaten = 0
    while k >= (h[0][0] - eaten) * len(h):
        k -= (h[0][0] - eaten) * len(h)
        eaten = heapq.heappop(h)[0]
    pos = k % len(h)
    h.sort(key=lambda x: x[1])

    return h[pos][1] + 1
