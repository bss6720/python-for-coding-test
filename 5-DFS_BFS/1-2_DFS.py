# DFS using recursion
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# can visit lower number node first
def dfs_stack(graph, v, visited):
    stack = [v]
    visited[v] = True
    print(v, end=' ')
    while len(stack) > 0:
        current = stack.pop()
        for next in graph[current]:
            if not visited[next]:
                stack.append(current)
                stack.append(next)
                visited[next] = True
                print(next, end=' ')
                break
    print()
# visits higher node first
def dfs_faster(graph,v):
    stack = [v]
    visited = set()
    while stack:
        next = stack.pop()
        if next not in visited:
            stack.extend(graph[next])
            visited.add(next)
            print(next, end=' ')


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

print('DFS using recursion')
dfs(graph, 1, visited)

visited = [False] * 9
print('\nDFS using stack')
dfs_stack(graph,1,visited)

print('\nDFS using set')
dfs_faster(graph,1)