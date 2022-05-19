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
-----------------------------------------------------------------------------------------------------------------------------
# simple code
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
