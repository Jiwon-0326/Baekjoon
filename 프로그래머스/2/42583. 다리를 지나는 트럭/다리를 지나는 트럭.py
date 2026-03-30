from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque([0]*bridge_length)
    bridge_weights = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights or bridge_weights > 0 :
        out = queue.popleft()
        bridge_weights -= out
        time += 1
        if truck_weights and bridge_weights + truck_weights[0] <= weight :
            now = truck_weights.popleft()
            queue.append(now)
            bridge_weights += now
        else :
            queue.append(0)
    
    return time
            
            

# 마지막 트럭 빠져나가는거 
    
    