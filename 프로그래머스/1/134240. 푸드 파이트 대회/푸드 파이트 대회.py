def solution(food):
    answer = ''
    
    for i in range(1, len(food)) :
        length = food[i] // 2
        for j in range(length) :
            answer += str(i)
        
    answer = answer + '0' + "".join(reversed(answer))
    
    return answer