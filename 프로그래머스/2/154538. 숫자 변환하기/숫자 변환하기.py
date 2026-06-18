def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)
    
    while s :
        if y in s :
            return answer
        s_cal = set()
        
        for i in s :
            if i + n <= y :
                s_cal.add(i+n)
                
            if i * 2 <= y :
                s_cal.add(i*2)
                
            if i * 3 <= y :
                s_cal.add(i*3)
            
        s = s_cal    
        answer += 1
    
    return -1