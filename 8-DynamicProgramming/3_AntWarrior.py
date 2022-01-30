import sys

n = int(sys.stdin.readline())
food_depots = list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(n)]

dp[0] = food_depots[0]
dp[1] = food_depots[1]
for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+food_depots[i])
print(dp[n-1])