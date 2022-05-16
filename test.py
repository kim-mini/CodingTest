def solution(answers):
    result = []
    SPJ1 = [1, 2, 3, 4, 5]
    SPJ2 = [2, 1, 2, 3, 2, 4, 2, 5]
    SPJ3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    rank = [0,0,0]
    passCnt = 0

    for i in range(len(answers)):
        ans1 = SPJ1[i % len(SPJ1)]
        ans2 = SPJ2[i % len(SPJ2)]
        ans3 = SPJ3[i % len(SPJ3)]

        if ans1 == answers[i]:
            rank[0] += 1
        if ans2 == answers[i]:
            rank[1] += 1
        if ans3 == answers[i]:
            rank[2] += 1
    passCnt = max(rank)
    for idx, cnt in enumerate(rank):
        if cnt == passCnt:
            result.append(idx+1)

    return result
