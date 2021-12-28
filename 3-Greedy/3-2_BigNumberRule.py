# changed user email
n,m,k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

tmp = m // (k+1)
remain = m%(k+1)

ans = data[-1]*tmp*k + data[-2]*tmp + data[-1]*remain
print(ans)