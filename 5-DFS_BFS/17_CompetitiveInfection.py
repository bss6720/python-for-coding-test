import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
tubes = []

for i in range(n):
    tubes.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())

# (time, virus_num)
candidates = []
if tubes[x-1][y-1] != 0:
    candidates.append((0,tubes[x-1][y-1]))
distances = [[-1] * n for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
que = deque()
que.append((x - 1, y - 1))
distances[x - 1][y - 1] = 0

while que:
    x_current, y_current = que.popleft()
    for i in range(4):
        x_next, y_next = x_current + dx[i], y_current + dy[i]
        if 0 <= x_next < n and 0 <= y_next < n:
            if distances[x_next][y_next] == -1:
                que.append((x_next, y_next))
                distances[x_next][y_next] = distances[x_current][y_current] + 1
                if tubes[x_next][y_next] != 0:
                    candidates.append((distances[x_next][y_next], tubes[x_next][y_next]))

candidates.sort()
if candidates[0][0] <= s:
    print(candidates[0][1])
else:
    print(0)
