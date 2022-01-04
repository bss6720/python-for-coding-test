# Turns Matrix 90 degree clockwise
def turn_list(l):
    length = len(l)
    turned = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            turned[i][j] = l[length - j - 1][i]
    return turned


# Check lock part and returns Boolean
def check_open(key_lock):
    lock_len = len(key_lock) // 3

    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            if key_lock[i][j] != 1:
                return False
    return True


# For debugging
def mat_print(matrix):
    for row in matrix:
        print(row)
    print()


def solution(key, lock):
    m = len(key)
    n = len(lock)
    # Create padded list
    padded = [[0] * (3 * n) for _ in range(3 * n)]

    # place lock inside padding
    for i in range(n):
        for j in range(n):
            padded[n + i][n + j] = lock[i][j]

    for turns in range(4):
        key = turn_list(key)
        for i in range(2 * n):
            for j in range(2 * n):
                # Add Key to padded Matrix
                for x in range(m):
                    for y in range(m):
                        # Made Stupid Mistake at j + y, used i instead of j
                        padded[i + x][j + y] += key[x][y]
                if check_open(padded):
                    return True
                # Remove Key from padded Matrix
                for x in range(m):
                    for y in range(m):
                        padded[i + x][j + y] -= key[x][y]

    return False


# Example Input
ex_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
ex_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(ex_key, ex_lock))
