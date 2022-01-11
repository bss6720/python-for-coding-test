def dfs(graph, v):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    connected = [0, 1, 2, 3]
    stack = [v]
    graph[v[0]][v[1]] = 1
    while stack:
        current = stack.pop()
        for i in range(4):
            pos_r = current[0] + dr[i]
            pos_c = current[1] + dc[i]
            if 0 <= pos_r < len(graph) and 0 <= pos_c < len(graph[0]):
                if graph[pos_r][pos_c] == 0:
                    stack.append(current)
                    stack.append((pos_r, pos_c))
                    graph[pos_r][pos_c] = 1
                    break


n, m = map(int, input().split())
ice_mold = []
for i in range(n):
    ice_mold.append(list(map(int, input())))
count = 0
for i in range(n):
    for j in range(m):
        if ice_mold[i][j] == 0:
            dfs(ice_mold, (i, j))
            count += 1
print(count)

# example input with answer 8
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111