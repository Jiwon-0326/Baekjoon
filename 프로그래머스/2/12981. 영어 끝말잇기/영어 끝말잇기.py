def solution(n, words):
    target_idx = 100
    answer = [0, 0]
    
    used = set()
    used.add(words[0])

    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in used:
            target_idx = i
            break
        used.add(words[i])
    
    
    if target_idx == 100 :
        return answer
    
    # 번호, 차례 구하기
    target_idx += 1
    if (target_idx % n) == 0 :
        answer[0] = n
    else :
        answer[0] = (target_idx % n)

    answer[1] = ((target_idx-1) // n) + 1
        
    return answer