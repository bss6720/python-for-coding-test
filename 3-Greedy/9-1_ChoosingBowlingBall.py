def fact(n):
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


def comb(n, r):
    if r > n:
        return 0
    return int(fact(n) / (fact(n - r) * fact(r)))


n, m = map(int, input().split())
data = list(map(int, input().split()))
count = [0 for i in range(m+1)]

for i in data:
    count[i] += 1

ans = comb(n,2)

for i in count[1:]:
    ans -= comb(i,2)

print(ans)