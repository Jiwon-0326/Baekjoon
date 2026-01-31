def solution(n, times):
    answer = 0
    
    left = 1
    right = n * max(times)      # 제일 오래 걸리는 심사관이 모든 사람을 처리할 경우
    
    while left <= right :
        sum = 0
        mid = (left + right) // 2
    
        for i in times : 
            sum += mid // i     # mid 시간동안 각 심사관이 처리할 수 있는 사람의 수를 합하기
        if sum >= n :       # mid 시간동안 처리할 수 있는 총 사람이 n명보다 많으면 시간을 줄이기
            answer = mid
            right = mid - 1
        else :              # mid 시간동안 처리할 수 있는 총 사람이 n명보다 적으면 시간을 늘리기
            left = mid + 1
    
    return answer