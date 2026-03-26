import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    
    time = 0    # 흐르는 시간
    answer = 0  # 반환 시간 누적
    i = 0       # jobs의 인덱스
    heap = []

    while i < n or heap :
        # 현재 시간까지 들어온 작업 넣기
        while i < n and jobs[i][0] <= time :
            # 소요시간, 요청시간 순서로 힙에 넣기 (우선순위대로)
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if heap :
            order_time, req_time = heapq.heappop(heap)  # heap에서 첫번째 원소 꺼내기
            time += order_time      # 소요시간만큼 시간 흐르기
            answer += (time - req_time)     # 반환시간 계산해서 누적
        else :      # 작업이 없으면 시간을 작업 요청 시간까지 점프
            time = jobs[i][0]
             
    return answer // n