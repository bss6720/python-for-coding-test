import sys
import heapq


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, current = heapq.heappop(hq)
        # means its already updated
        if distance[current] < dist:
            continue
        for i in graph[current]:
            if i[1] + dist < distance[i[0]]:
                distance[i[0]] = i[1] + dist
                heapq.heappush(hq, (distance[i[0]], i[0]))


INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, v, e = map(int, sys.stdin.readline().split())
    graph[u].append((v, e))

distance = [INF] * (n + 1)
dijkstra(start)

for i in range(1,n+1):
    if distance == INF:
        print("INFINITY")
    else:
        print(distance[i])