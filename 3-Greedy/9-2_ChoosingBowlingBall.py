n, m = map(int, input().split())
data = list(map(int, input().split()))
count = [0 for i in range(m + 1)]
# counts each coins
for i in data:
    count[i] += 1
ans = 0
# starting from 1, adds possible combinations
for i in range(1, m + 1):
    n -= count[i]
    ans += (count[i] * n)
print(ans)
