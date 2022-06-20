def solution(money):
    coin = [5,2]
    count = 0

    while (money != 0):
        if money % 5 == 0:
            money -= coin[0]
            count += 1
        else:
            money -= coin[1]
            count += 1
    return count
