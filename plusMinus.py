def solution(absolutes, signs):
    answer = 0
    for i in absolutes:
        if signs[absolutes.index(i)]:
            answer += i
        else:
            answer -= i
    return answer
