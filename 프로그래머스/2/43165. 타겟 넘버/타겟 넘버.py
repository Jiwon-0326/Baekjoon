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
    
    return leaves.count(target)