def solution(N, stages):
    answer = [0 for i in range(N+1)]
    for i in stages:
        answer[i - 1] += 1
    count = len(stages)
    arr = []
    for i in range(N):
        if count == 0:
            continue
        answer[i], count = answer[i] / count, count - answer[i]
        arr.append((i, answer[i]))
    sorted(arr, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in arr]

    return answer
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))