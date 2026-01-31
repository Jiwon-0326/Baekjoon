from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)) :
        k_ = k
        tmp = 0
        for i, j in p :
            if k_ >= i :
                k_ -= j
                tmp += 1
        if tmp >= answer : 
            answer = tmp           
    return answer