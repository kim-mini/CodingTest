def solution(N, stages):
    answer = []
    fail = {}
    all = len(stages)

    for i in range(1,N+1):
        if all != 0:
            count = stages.count(i)
            fail[i] = count / all
            all -= count
        else:
            fail[i] = 0

    return sorted(fail, key=lambda x:fail[x],reverse=True)
