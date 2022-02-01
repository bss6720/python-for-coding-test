import sys

n, m = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort()
dp = [-1 for i in range(m + 1)]
dp[0] = 0
for i in range(coins[0], m + 1):
    count = 10001
    for coin in coins:
        if dp[i - coin] != -1:
            count = min(dp[i - coin] + 1, count)
    if count != 10001:
        dp[i] = count
print(dp[m])
