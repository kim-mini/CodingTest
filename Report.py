def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dicReports = {id:[] for id in id_list}

    for i in set(report):
        people = i.split(" ")
        dicReports[people[1]].append(people[0])

    for key, value in dicReports.items():
        if (len(value) >= k):
            for j in value:
                answer[id_list.index(j)] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
answer = solution(id_list, report, k)
print(answer)

