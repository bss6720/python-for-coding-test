# Programmers 30/lessons/42889
def solution(N, stages):
    arr = [0 for i in range(N)]
    answer = []
    for i in stages:
        if i == N + 1:
            continue
        arr[i - 1] += 1
    count = len(stages)
    for i in range(N):
        if count == 0:
            answer.append((i, 0))
        else:
            answer.append((i, arr[i] / count))
        count -= arr[i]

    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0]+1 for i in answer]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
