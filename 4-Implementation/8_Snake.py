# BOJ 3190

import sys
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
n = int(input())
k = int(input())
# create map with padding
snake_map = [[-1] + ([0] * n) + [-1] for i in range(n + 2)]
# padding top and bottom
for i in range(n + 2):
    snake_map[0][i] = -1
    snake_map[n + 1][i] = -1

# input apple
for i in range(k):
    ar, ac = map(int, input().split())
    snake_map[ar][ac] = 1

L = int(input())
turns = []
for i in range(L):
    new_input = sys.stdin.readline().rstrip().split()
    sec_later = int(new_input[0])
    direction = new_input[1]
    turns.append((sec_later, direction))

snake = deque([(1, 1)])
heading = 0
time = 0
turn_index = 0
while True:
    time += 1
    r_new = snake[0][0] + dr[heading]
    c_new = snake[0][1] + dc[heading]
    if (r_new,c_new) in snake:
        break
    elif snake_map[r_new][c_new] == 1:
        snake_map[r_new][c_new] = 0
        snake.appendleft((r_new, c_new))
    elif snake_map[r_new][c_new] == 0:
        snake.appendleft((r_new, c_new))
        snake.pop()
    elif snake_map[r_new][c_new] == -1:
        break
    # Turning Snake's Direction
    if turn_index < len(turns):
        if turns[turn_index][0] == time:
            if turns[turn_index][1] == 'D':
                heading = (heading + 1) % 4
            elif turns[turn_index][1] == 'L':
                heading = (heading - 1) % 4
            turn_index += 1
print(time)
