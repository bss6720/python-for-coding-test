# Baekjoon Online Judge 1439
string = input()
zero_group = 0
one_group = 0
prev = string[0]
for i in string:
    if i == prev:
        continue
    else:
        if prev == '0':
            zero_group += 1
        elif prev == '1':
            one_group += 1
        prev = i
print(max(zero_group, one_group))
