def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    # 모든 경우의 수 계산하기
    for num in numbers :
        temp = []
        
        for leaf in leaves :
            temp.append(leaf + num)
            temp.append(leaf - num)
            
        leaves = temp
    
    # 모든 경우의 수 중 타겟과 같은 개수 세기
    for i in leaves :
        if i == target :
            answer += 1
    
    return answer