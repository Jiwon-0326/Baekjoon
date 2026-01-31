def solution(n, times):
    answer = 0
    left = 1
    right = n * max(times)
    
    while left <= right :
        sum = 0
        mid = (left + right) // 2
        
        for i in times : 
            sum += mid // i
        if sum >= n :
            answer = mid
            right = mid - 1
        else : 
            left = mid + 1
    
    return answer