def solution(numbers, target):
    leaves = [0]
    
    for n in numbers :
        temp = []
        
        for leaf in leaves :
            temp.append(leaf + n)
            temp.append(leaf - n)
        
        leaves = temp
    
    return leaves.count(target)