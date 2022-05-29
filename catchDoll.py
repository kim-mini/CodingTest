def solution(board, moves):
    answer = 0
    board = board
    box = []
    scr, dst = 0,0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            box.append(board[j][i-1])
            if len(box) > 1:
                scr = len(box)-1
                dst = len(box)-2
                if box[scr] == box[dst]:
                    box = box[:dst]
                    answer += 2
                    break
            else :
                scr = 0
                dst = 0
                break
    return answer
