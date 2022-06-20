def solution(board, point, way, monster):
    if way == 0:
        go = True
    else:
        go = False

    for i in range(1,board[0]+1):
        if go:
            for j in range(1,board[1]+1):
                if i == monster[0] and j == monster[1]:
                    return  print("NO...")
        else:
            for j in reversed(range(1, board[1]+1)):
                if i == monster[0] and j == monster[1]:
                    return print("NO...")

        go = not(go)

    return print("YES!")
