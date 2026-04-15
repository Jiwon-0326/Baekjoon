def solution(arr, idx):    
    for i, x in enumerate(arr) :
        if x == 1 and i >= idx :
            return i
    return -1