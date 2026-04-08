def solution(s):
    answer = []
    zeroCnt = 0
    cnt = 0
    
    while s != '1' :
        zeroCnt += s.count('0')
        
        s = s.replace("0",'')   
        s = bin(len(s))[2:] 
        
        cnt +=1
        
    answer = [cnt, zeroCnt]
    return answer