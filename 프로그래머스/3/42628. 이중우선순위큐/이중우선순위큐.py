import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations :
        if op[0] == 'I' :
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif op == 'D -1' :       # 최솟값 삭제
            if min_heap : 
                min_num = heapq.heappop(min_heap)   # 최소힙에서 제거
                max_heap.remove(-min_num)       # 최대힙에서 제거
                heapq.heapify(max_heap)
        elif op == 'D 1' :      # 최댓값 삭제
            if max_heap :
                max_num = heapq.heappop(max_heap)       # 최대힙에서 제거
                min_heap.remove(-max_num)           # 최소힙에서 제거
                heapq.heapify(min_heap)

    if min_heap :
        return [-max_heap[0], min_heap[0]]
    else :
        return [0,0]
