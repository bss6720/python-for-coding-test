# BOJ 18406
n = input()
half = int(len(n) / 2)

l_sum = 0
r_sum = 0
for i in range(half):
    l_sum += int(n[i])
    r_sum += int(n[i + half])

if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")
