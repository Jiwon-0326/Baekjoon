from collections import deque

def solution(bridge_length, weight, truck_weights):
    # (트럭의 최대 대수, 최대 무게, 트럭별 무게)
    queue = deque([0]*bridge_length)       # 다리
    time = 0                # 시간
    bridge_weigh = 0        # 현재 다리 위 트럭 무게 합
    truck_weights = deque(truck_weights)
    
    while truck_weights or bridge_weigh > 0 :
        out = queue.popleft()
        bridge_weigh -= out
        if truck_weights and bridge_weigh + truck_weights[0] <= weight :   # 다리에 트럭이 들어갈 수 있을 때
            truck_now = truck_weights.popleft()
            queue.append(truck_now)
            bridge_weigh += truck_now
            time += 1
        else :              # 다리에 트럭이 못 들어갈 때
            queue.append(0)
            time += 1  
    
    return time