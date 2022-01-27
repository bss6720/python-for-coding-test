# Programmers 30/lessons/60061

def check_possible(x, y, a, answer):
    # bearing
    if a:
        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
            return True
    # pillar
    else:
        if y == 0 or [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer:
            return True
    # not possible to place
    return False


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # create
        if b:
            if check_possible(x, y, a,answer):
                answer.append([x, y, a])
        # delete
        else:
            answer.remove([x, y, a])
            possible = True
            for tx, ty, ta in answer:
                if not check_possible(tx, ty, ta,answer):
                    possible = False
                    break
            if not possible:
                answer.append([x, y, a])
    answer.sort()
    return answer


# build_frame = [[x,y,a,b]]
# x,y - coordinate
# a - 0 for pillar, 1 for bearing
# b - 0 for delete, 1 for create

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
