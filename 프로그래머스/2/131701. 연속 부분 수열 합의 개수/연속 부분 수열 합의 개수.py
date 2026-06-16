def solution(elements):
    answer = []
    answer.append(sum(elements))
    arr = elements * 2

    for length in range(1, len(elements)) :
        for start in range(len(elements)) :
            answer.append(sum(arr[start:start+length]))
            
    sums = set(answer)
    return len(sums)