def keyPadDist(culNum, num):
    numPad = {1:[0,0],2:[1,0],3:[2,0],
              4:[0,1],5:[1,1],6:[2,1],
              7:[0,2],8:[1,2],9:[2,2],
              '*':[0,3],0:[1,3],'#':[2,3]}

    x1, y1 = numPad[culNum]
    x2, y2 = numPad[num]

    return abs(x1-x2)+abs(y1-y2)


def solution(numbers, hand):
    answer = ''
    culNumL, culNumR = 0, 0

    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            culNumL = i
        elif i in [3, 6, 9]:
            answer += 'R'
            culNumR = i
        else:
            if keyPadDist(culNumR, i) > keyPadDist(culNumL, i):
                answer += 'L'
                culNumL = i
            elif keyPadDist(culNumR, i) < keyPadDist(culNumL, i):
                answer += 'R'
                culNumR = i
            elif keyPadDist(culNumR, i) == keyPadDist(culNumL, i):
                if hand == 'right':
                    answer += 'R'
                    culNumR = i
                else:
                    answer += 'L'
                    culNumL = i
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand ="right"

print(solution(numbers, hand))


