# Programmers course 30, lessons 42891
# Faster but, complicated, easy to make mistake
def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1
    sort_food = sorted(food_times, reverse=True)
    eaten_one = 0
    while k >= ((sort_food[-1] - eaten_one) * len(sort_food)):
        k -= ((sort_food[-1] - eaten_one) * len(sort_food))
        eaten_one = sort_food[-1]
        sort_food.pop()
    pos = (k) % len(sort_food)
    tmp = -1
    for i in range(len(food_times)):
        if (food_times[i] - eaten_one) > 0:
            tmp += 1
            if tmp == pos:
                answer = i + 1
                break

    return answer
