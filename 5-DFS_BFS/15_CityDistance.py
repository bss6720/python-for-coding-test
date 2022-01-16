# BOJ 18352

import sys
from collections import deque


def bfs(graph, start, k):
    distance = [-1 for i in range(len(graph))]
    cities = []
    que = deque()
    que.append(start)
    distance[start] = 0
    while que:
        current = que.popleft()
        for i in graph[current]:
            if distance[i] == -1:
                que.append(i)
                distance[i] = distance[current] + 1
    for i in range(len(distance)):
        if distance[i] == k:
            cities.append(i)
    return cities


n, m, k, x = map(int, input().split())
edges = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)

ans = bfs(edges,x,k)
if ans:
    for i in ans:
        print(i)
else:
    print('-1')