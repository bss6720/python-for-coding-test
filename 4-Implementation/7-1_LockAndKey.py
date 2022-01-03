# Programmers learn/courses/30/lessons/60059
def turn(k):
    turned = []
    leng = len(k)
    for i in range(leng):
        turned.append([])
        for j in range(leng):
            turned[i].append(k[leng - j - 1][i])
    return turned


def check_key(lock):
    lock_len = len(lock) // 3
    for i in range(lock_len, 2 * lock_len):
        for j in range(lock_len, 2 * lock_len):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = turn(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check_key(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False
