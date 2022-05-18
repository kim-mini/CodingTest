def solution(n, lost, reserve):
    answer = 0
    classMate = [1] * n

    for i in lost:
        classMate[i-1] = 0

    for pre in reserve:
        classMate[pre-1] = 2

    for mate in range(len(classMate)):
        if classMate[mate] == 0 or classMate[mate] == 1:
            continue
        elif mate != len(classMate)-1 and classMate[mate] == 2 and classMate[mate + 1] < 1:
             classMate[mate] -= 1
             classMate[mate + 1] += 1
        elif mate != 0 and classMate[mate] == 2 and classMate[mate - 1] < 1:
             classMate[mate] -= 1
             classMate[mate - 1] += 1

    for i in classMate:
        if i > 0:
            answer += 1

    return answer
