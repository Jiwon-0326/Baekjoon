from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    # BFS
    queue = deque([1])
    distance[1] = 0
    
    while queue :
        now = queue.popleft()
        for i in graph[now] :
            if distance[i] == -1 :
                queue.append(i)
                distance[i] = distance[now] + 1
    
    # 최대값 개수
    answer = 0
    max_dist = max(distance)
    for d in distance :
        if d == max_dist :
            answer += 1
    
    return answer