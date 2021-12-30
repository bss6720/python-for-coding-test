#     N,E,S,W order
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
n, m = map(int, input().split())
xpos, ypos, direction = map(int, input().split())
gmap = []
for _ in range(n):
    gmap.append(list(map(int, input().split())))

# sea=1, land not visited=0, land visited=2
gmap[xpos][ypos] = 2
while True:
    noMove = True
    # Checks all Four Directions
    for i in range(1, 5):
        tmpDir = (direction - i) % 4
        xtmp = xpos + dx[tmpDir]
        ytmp = ypos + dy[tmpDir]
        # if Not Visited Exists, Move
        if gmap[xtmp][ytmp] == 0:
            noMove = False
            xpos = xtmp
            ypos = ytmp
            gmap[xpos][ypos] = 2
            count += 1
            direction = tmpDir
            break
    # If All Four Directions visited
    if noMove:
        back = (direction - 2) % 4
        xtmp = xpos + dx[back]
        ytmp = ypos + dy[back]
        # if Back is Sea, Full Stop
        if gmap[xtmp][ytmp] == 1:
            break
        # Going Back
        else:
            xpos = xtmp
            ypos = ytmp
            count += 1

print(count)
