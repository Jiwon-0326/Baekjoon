def solution(prices):
    l = len(prices)
    answer = [0] * l
    stack = []
    
    for i in range(l) :
        while stack and prices[stack[-1]] > prices[i] :
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = l - 1 - j
    
    return answer
            
    
    return answer 