def solution(prices):
    l = len(prices)
    answer = []
    for i in range(l) :
        answer.append(l-i-1)
        for j in range(i+1, l) :
            if prices[i] > prices[j] :
                answer[i] = j-i
                break
        
    return answer