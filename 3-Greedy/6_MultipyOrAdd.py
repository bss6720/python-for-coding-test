num = input()
ans = int(num[0])
for i in num[1:]:
    nextNum = int(i)
    # if either of them are 1 or 0, then it's better to add than multiply
    if nextNum <= 1 or ans <= 1:
        ans += nextNum
    else:
        ans *= nextNum
print(ans)
