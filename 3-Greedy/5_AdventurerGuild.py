n = int(input())
fearData = list(map(int, input().split()))
fearData.sort()

group = 0
count = 0
for i in fearData:
    count += 1
    # if last member's fear data is lesser or equal to current count, then it becomes another group
    if count >= i:
        group += 1
        count = 0
print(group)
