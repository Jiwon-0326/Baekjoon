def solution(a, b, n):
    answer = 0
    
    while n >= a :
        if n // a == 0 :
            bottle = (n // a) * b
            answer += bottle
            n = bottle
        else :
            bottle = ((n - (n % a)) // a ) * b
            answer += bottle
            n = bottle + (n % a)
            
    return answer