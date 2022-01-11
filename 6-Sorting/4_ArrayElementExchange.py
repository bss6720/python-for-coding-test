n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
count = 0
for i in range(k):
    if b[i]>a[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))