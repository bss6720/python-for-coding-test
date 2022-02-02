# Dijkstra work for positive edges
# Uses int(1e9) for infinity
import sys


# Returns not visited shortest distance Node
def get_smallest_node():
    selected = 0
    for i in range(1, n + 1):
        if distance[i] < distance[selected] and not visited[i]:
            selected = i
    return selected


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # Initialize distance table with start node
    for j in graph[start]:
        distance[j[0]] = j[1]
    for j in range(n - 1):
        current = get_smallest_node()
        visited[current] = True
        for k in graph[current]:
            # If current path is shorter
            distance[k[0]] = min(distance[k[0]], distance[current] + k[1])


INF = int(1e9)
# Node count, Edge count
n, m = map(int, sys.stdin.readline().split())
# start Node
start = int(sys.stdin.readline())
# graph in form of graph[node] = (to,distance)
graph = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
# Initialize distance to Nodes table to INF
distance = [INF for i in range(n + 1)]

for i in range(m):
    u, v, e = map(int, sys.stdin.readline().split())
    graph[u].append((v, e))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# test input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
