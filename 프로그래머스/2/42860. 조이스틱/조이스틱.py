def solution(name):
    answer = 0    
    for x in name :
        cnt = ord(x) - ord('A')
        if cnt < 13 :
            answer += cnt
        else :
            answer += (26-cnt)
        
    # 좌우 이동
    move = len(name) - 1

    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        move = min(move, i * 2 + len(name) - next, i + 2 * (len(name) - next))
    answer += move
    
    return answer