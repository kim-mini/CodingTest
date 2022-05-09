def solution(s):
    answer = 0
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numDic = {}
    num = ''
    word = []

    for i in range(10):
        numDic[en[i]] = i

    for j in s:
        if j.isdigit():
            word.append('%s' %j)
        else:
            num = num + j
            if (num in numDic.keys()):
                word.append('%s' % numDic[num])
                num = ''
    answer = int(''.join(word))
    return answer

s = "23four5six7"
print(solution(s))


