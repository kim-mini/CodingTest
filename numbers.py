def solution(left, right):
    answer = 0
    numbers = []

    for num in range(left,right+1):
        for i in range(1,num+1):
            if num % i == 0:
                numbers.append(i)
        if len(numbers) %2 == 0:
            answer += num
        else:
            answer -= num

        numbers = []
        
    return answer
