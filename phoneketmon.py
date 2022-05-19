// min을 활용한 한줄코드
def solution(nums):
    answer = min(len(set(nums)), len(nums)/2)
    return answer

  
----------------------------------------------------------------------------------------


def solution(nums):
    answer = 0
    mon = len(nums) /2
    phonket = len(set(nums))
    if mon > phonket:
        answer = phonket
    else:
        answer = mon

    return int(answer)
  
  
  
  
  
