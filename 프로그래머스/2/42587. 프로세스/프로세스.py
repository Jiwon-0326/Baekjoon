from collections import deque

def solution(priorities, location):
    answer = 0
    
    reload = deque()
    for i, p in enumerate(priorities) :
        reload.append((p, i))
    
    while 1 :
        temp = reload.popleft()
        
        if any(temp[0] < i[0] for i in reload) :
            reload.append(temp)
        else : 
            answer += 1
            if temp[1] == location : 
                return answer
