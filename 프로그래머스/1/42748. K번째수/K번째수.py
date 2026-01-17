def solution(array, commands):
    answer = []
    
    # 배열 자르고 정렬    
    for i in range(len(commands)) :
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
    
        # k번째 수 구하기
        answer.append(arr[commands[i][2]-1])
    
    return answer