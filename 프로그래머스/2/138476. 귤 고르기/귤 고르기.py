from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    result = sorted(counter.values(), reverse=True)
    
    count = 0
    answer = 0
    
    for i in result :
        count += i
        answer += 1
        if count >= k :
            return answer