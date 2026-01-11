import math 

def solution(progresses, speeds):
    days = []
    for i, x in enumerate(progresses) :
        days.append(math.ceil((100-x)/speeds[i]))
        
    count = 1
    answer = []
    for i in range(len(days)-1) : 
        if days[i+1] > days[i] :
            answer.append(count)
            count = 1
        else :
            days[i+1] = days[i]
            count += 1
    answer.append(count)
    return answer
