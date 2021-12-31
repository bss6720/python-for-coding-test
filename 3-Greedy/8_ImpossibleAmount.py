n = int(input())
coins = list(map(int, input().split()))
coins.sort()

# if you can make target, then you can make till target+newNumber
target = 1
for i in coins:
    # if newNumber is greater than target, there is no way to make target
    if target < i:
        break
    target += i
print(target)
