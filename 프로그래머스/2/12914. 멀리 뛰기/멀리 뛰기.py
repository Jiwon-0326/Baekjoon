import math


def solution(n):
    answer = 0
    two_div = n // 2

    for i in range(two_div + 1):
        if i == 0 :
            answer += 1
        else:
            left = n - (2*i)
            answer += math.comb(i + left, i)

    answer %= 1234567        

    return answer