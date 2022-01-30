import sys


def operation(a, b, i):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    else:
        return int(a / b)


def solution(index, total):
    if index < n:
        for i in range(4):
            if oper_arr[i]:
                oper_arr[i] -= 1
                solution(index + 1, operation(total, arr[index], i))
                oper_arr[i] += 1
    else:
        global min_total, max_total
        min_total = min(min_total, total)
        max_total = max(max_total, total)


def solution2(index, total, plus, minus, multiply, divide):
    if index >= n:
        global min_total, max_total
        min_total = min(min_total, total)
        max_total = max(max_total, total)
        return
    if plus:
        solution2(index + 1, total + arr[index], plus - 1, minus, multiply, divide)
    if minus:
        solution2(index + 1, total - arr[index], plus, minus - 1, multiply, divide)
    if multiply:
        solution2(index + 1, total * arr[index], plus, minus, multiply - 1, divide)
    if divide:
        solution2(index + 1, int(total / arr[index]), plus, minus, multiply, divide - 1)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
oper_arr = list(map(int, sys.stdin.readline().split()))
min_total = 1000000001
max_total = -1000000001
# solution(1,arr[0])
solution2(1, arr[0], oper_arr[0], oper_arr[1], oper_arr[2], oper_arr[3])
print(max_total)
print(min_total)
