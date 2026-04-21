def solution(n):
    answer = 1
    a = 2
    
    while (a*(a+1)) <= (2*n)  :
        temp = n - (a*(a-1) // 2)
            
        if (temp % a) == 0 :
            answer += 1
        
        if temp / a == 1 :
            break 
        a += 1
        
    return answer