import sys

n = int(input())

houses = list(map(int, sys.stdin.readline().split()))
houses.sort()

left = 0
right = n
cost = sum(houses)
min_cost = cost
pos = houses[0]
for i in range(n):
    cost += left*houses[i]
    cost -= right*houses[i]
    if cost < min_cost:
        min_cost = cost
        pos = houses[i]
    left += 1
    right -= 1
print(pos)
