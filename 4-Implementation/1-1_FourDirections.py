r, c = 1, 1
n = int(input())
directions = input().split()

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']
for i in directions:
    op = moveTypes.index(i)
    tr, tc = r + dr[op], c + dc[op]
    if 1 <= tr <= n and 1 <= tc <= n:
        r, c = tr, tc

print(r, c)
