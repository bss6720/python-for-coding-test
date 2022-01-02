# Programmers learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[:i]
        count = 0
        j = 0
        for j in range(0, len(s), i):
            if prev == s[j:j + i]:
                count += 1
            else:
                if count != 1:
                    prev = str(count) + prev
                compressed = compressed + prev
                count = 1
                prev = s[j:j + i]
        if count != 1:
            prev = str(count) + prev
        compressed = compressed + prev

        # print(compressed)
        answer = min(len(compressed), answer)
    return answer
