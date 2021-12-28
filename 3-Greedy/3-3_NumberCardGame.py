# changed user email
n,m = map(int, input().split())

maxMin=0
for i in range(n):
    data = min(list(map(int, input().split())))
    maxMin = max(maxMin,data)
print(maxMin)