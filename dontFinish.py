def solution(participant, completion):
    answer = ''
    temp = 0
    whoIs = {}

    for part in participant:
        whoIs[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = whoIs[temp]
    return answer
