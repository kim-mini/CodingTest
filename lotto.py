def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    cnt = 0
    decnt = 0
    for i in lottos:
        for j in win_nums:
            if (i==j):
                cnt=cnt+1

        if(i==0):
            decnt=decnt+1

    answer[0]= rank[cnt+decnt]
    answer[1]= rank[cnt]
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
answer = solution(lottos,win_nums)
print(answer)
