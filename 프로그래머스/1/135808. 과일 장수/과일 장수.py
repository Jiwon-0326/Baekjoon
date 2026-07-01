def solution(k, m, score):
    length = len(score) // m
    score.sort()
    answer = 0
    
    for i in range(length) :
        arr = []
        for j in range(m) :
            arr.append(score.pop())
        answer += min(arr) * m
    
    return answer