from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(graph, v, visited):
    que = deque()
    que.append(v)
    visited[v[0]][v[1]] = 1
    while que:
        current = que.popleft()
        for i in range(4):
            r_next = current[0] + dr[i]
            c_next = current[1] + dc[i]
            if 0 <= r_next < n and 0 <= c_next < m:
                if visited[r_next][c_next] == 0 and maze[r_next][c_next] == 1:
                    que.append((r_next,c_next))
                    visited[r_next][c_next] = visited[current[0]][current[1]] + 1


n, m = map(int, input().split())
maze = []
visited = [[0] * m for i in range(n)]

for i in range(n):
    maze.append(list(map(int, input())))

bfs(maze,(0,0),visited)
print(visited[n-1][m-1])
for row in visited:
    print(row)

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111