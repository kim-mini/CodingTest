def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]-1
        j = com[1]
        k = com[2] -1

        dsc = array[i:j]
        dsc.sort()
        answer.append(dsc[k])
    return answer
