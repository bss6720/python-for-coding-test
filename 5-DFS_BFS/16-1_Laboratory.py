import sys
from collections import deque


def copy_matrix(a):
    out = []
    for row in a:
        out.append(row.copy())
    return out


def count_safe(array):
    count = 0
    for row in array:
        count += row.count(0)
    return count


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(array, v):
    que = deque()
    que.append(v)
    while que:
        current = que.popleft()
        for i in range(4):
            x, y = current[0] + dr[i], current[1] + dc[i]
            if not (0 <= x < n and 0 <= y < m):
                continue
            if array[x][y] == 0:
                array[x][y] = 2
                que.append((x, y))


def full_search(count):
    global result
    if count == 3:
        temp = copy_matrix(lab)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    bfs(temp, (i, j))
        result = max(result, count_safe(temp))
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                full_search(count)
                lab[i][j] = 0
                count -= 1


n, m = map(int, sys.stdin.readline().rstrip().split())
result = 0
lab = []

for i in range(n):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))

full_search(0)
print(result)
