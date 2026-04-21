def solution(s):
    s = s.split()
    s_arr = []
    
    for x in s :
        s_arr.append(int(x))
            
    answer = str(min(s_arr)) + ' ' + str(max(s_arr))
    return answer