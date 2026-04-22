def solution(n):
    answer = ''
    
    while n > 0:
        n, remainder = divmod(n, 3)
        
        if remainder == 0:
            answer = '4' + answer
            n -= 1
        elif remainder == 1:
            answer = '1' + answer
        else:  # remainder == 2
            answer = '2' + answer
            
    return answer


#                          몫        나머지
# 123         1 2 4       0 0 1     1 2 0    

# 456        11 12 14     1 1 2     1 2 0
# 789        21 22 24     2 2 3     1 2 0
# 101112     41 42 44     3 3 4

# 131415    111 112 114   4 4 5
# 161718
