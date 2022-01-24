# BOJ 1715
import heapq
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline()))

total = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    a += heapq.heappop(arr)
    total += a
    heapq.heappush(arr, a)

print(total)
