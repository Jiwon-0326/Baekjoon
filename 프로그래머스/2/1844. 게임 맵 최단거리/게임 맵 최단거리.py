from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 , 0]
    
    queue = deque()
    queue.append((0,0))
    
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            
            if maps[nx][ny] == 1 :
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    
    if maps[n-1][m-1] == 1 :
        return -1
    
    return maps[n-1][m-1]
    