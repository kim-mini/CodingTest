def solution(N, stages):
    answer = []
    fail = {}
    all = len(stages)

    for i in range(N):
        fail[i+1] = stages.count(i+1) / all
        all -= stages.count(i+1)

    return sorted(fail, key=lambda x:fail[x],reverse=True)
