def factorial_iter(n):
    ans = 1
    # multiplicates from 1 to n
    for i in range(1, n + 1):
        ans *= i
    return ans


def factorial_recur(n):
    # terminate condition
    if n <= 1:
        return 1
    else:
        # Written code in form of n! = n * (n-1)!
        return n * factorial_recur(n - 1)


print('반복적으로 구현:', factorial_iter(5))
print('재귀적으로 구현:', factorial_recur(5))
