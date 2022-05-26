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



--------------------------------------------------------------------------------------------------------------

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    stop = {x:0 for x in id_list}

    for i in set(report):
        stop[i.split()[1]] += 1

    for j in set(report):
        if stop[j.split()[1]] >= k:
            answer[id_list.index(j.split()[0])] += 1

    return answer

