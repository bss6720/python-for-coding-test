word = list(input())
count = 0
ans = []
for i in range(len(word)):
    if word[i].isdigit():
        count += int(word[i])
    else:
        ans.append(word[i])
ans.sort()
ans.append(str(count))
print(''.join(ans))
