def solution(storey):
    answer = 0
    while storey >= 1 :
        storey, remainder = divmod(storey, 10)
        if remainder == 5 :
            temp = storey % 10
            if temp >= 5 :
                answer += (10 - remainder)
                storey += 1
            else :
                answer += remainder
        elif remainder > 5 :
            answer += (10 - remainder)
            storey += 1
        else :
            answer += remainder
        
    return answer