def solution(jobs):
    jobs.sort()  # 요청 시간 기준 정렬
    time = 0
    answer = 0
    waiting = []
    job_len = len(waiting) + len(jobs)
    
    while jobs or waiting:
        # 현재 시간까지 들어온 작업 넣기
        while jobs and jobs[0][0] <= time:
            waiting.append(jobs.pop(0))
        
        if waiting:
            waiting.sort(key=lambda x: x[1])  # 소요시간 기준
            job = waiting.pop(0)
            time += job[1]
            answer += time - job[0]
        else:
            # 작업 없으면 시간 점프
            time = jobs[0][0]
    
    return answer // job_len  # 평균