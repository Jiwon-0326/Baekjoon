def solution(citations):
    citations.sort()
    l = len(citations)
    answer = 0
    
    for i, n in enumerate(citations) :
        if min(n, l-i) > answer : answer = min(n, l-i)
    
    return answer
