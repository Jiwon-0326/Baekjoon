from itertools import permutations       # 선언 꼭 하기!

# 소수인지 판별
def prime(num_case):
    prime_count = 0
    for n in num_case :
        count = 0
        for i in range(2, n) :
            if n % i == 0 : 
                count += 1
                break
        if n > 1 and count == 0 :
            prime_count += 1
    return prime_count

# 모든 경우의 수 찾기
def solution(numbers):
    num_case = []
    for i in range(1, len(numbers)+1) :     # 1부터 숫자의 개수만큼
        tmp = permutations(numbers, i)     # 순열로 모든 경우 뽑기
        for j in tmp :
            tmp_str = "".join(j)        # 결과를 한 문자열로 합치기
            num_case.append(int(tmp_str))       # int로 변환하여 리스트에 추가
    num_case = list(set(num_case))      # 중복 제거
    return prime(num_case)