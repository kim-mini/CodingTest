import re

def solution(new_id):
    answer = ''
    # 1st
    new_id = new_id.lower()
    # 2nd
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in '-_.':
            answer = answer+i
    # 3rd
    while '..' in answer:
        answer = answer.replace('..','.')
    # 4rd

    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer

    answer = answer[:-1] if answer[-1] == '.' else answer

    # 5rd
    answer = 'a' if answer =='' else answer

    # 6rd
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7rd
    if len(answer) <= 3:
        answer = answer+answer[-1]*(3-len(answer))
    return answer

new_id ="abcdefghijklmn.p"
print(solution(new_id))
