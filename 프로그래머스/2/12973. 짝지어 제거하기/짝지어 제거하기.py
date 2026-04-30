def solution(s):
    s_new = []
    
    for char in s :
        if s_new and s_new[-1] == char :
            s_new.pop()
        else :
            s_new.append(char)
    

    if len(s_new) == 0 :
        return 1
    else :
        return 0