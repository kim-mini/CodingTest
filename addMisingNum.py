def solution(numbers):
    answer = 0

    for i in range(10):
        if i in numbers:
            continue
        answer += i

    return answer

numbers = [5,8,4,0,6,7,9]

print(solution(numbers))
