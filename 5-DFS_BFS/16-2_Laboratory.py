# BOJ 14502

import sys
from itertools import combinations


def copy_matrix(array):
    copied = []
    for row in array:
        copied.append(row.copy())
    return copied


def count_safe(array=list()):
    n = len(array)
    count = 0
    for i in range(n):
        count += array[i].count(0)
    return count


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def spread(v):
    for i in range(4):
        x = v[0] + dr[i]
        y = v[1] + dc[i]
        if not (0 <= x < n and 0 <= y < m):
            continue
        if temp[x][y] == 0:
            temp[x][y] = 2
            spread((x, y))


def full_search(array, n, m):
    result = 0
    global temp
    # map_idx = [(i, j) for i in range(n) for j in range(m)]
    # empty spaces
    map_idx = []
    # 2 indexes
    virus = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:
                virus.append((i, j))
            elif array[i][j] == 0:
                map_idx.append((i, j))

    for walls in combinations(map_idx, 3):
        temp = copy_matrix(array)
        # make 3 walls
        for pos in walls:
            temp[pos[0]][pos[1]] = 1

        for i in virus:
            spread(i)
        result = max(result, count_safe(temp))

    return result


n, m = map(int, sys.stdin.readline().split())
lab = []
temp = []
for i in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))

print(full_search(lab, n, m))
