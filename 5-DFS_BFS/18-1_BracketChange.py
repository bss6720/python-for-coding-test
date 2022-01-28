# Programmers 30/lessons/60058

def solution(p):
    # return empty string
    if p == '':
        return ''
    # divide p into u and v where u is balanced bracket string
    bk_open = 0
    bk_close = 0
    v = 0
    for i in range(len(p)):
        if p[i] == '(':
            bk_open += 1
        else:
            bk_close += 1
        v = i + 1
        if bk_open == bk_close:
            break
    # It is balanced bracket string
    # (There always is a balanced bracket string according to the Question)
    if bk_open == bk_close:
        # Check if it's Proper bracket string
        stack = []
        for i in range(v):
            if stack != []:
                if stack[-1] != p[i] and p[i] == ')':
                    stack.pop()
                    continue
            stack.append(p[i])
        # It is Proper bracket string
        if stack == []:
            return p[:v] + solution(p[v:])
        else:
            u = ''
            for x in p[1:v - 1]:
                if x == '(':
                    u = u + ')'
                else:
                    u = u + '('
            return '('+solution(p[v:])+')'+u


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution('()'))