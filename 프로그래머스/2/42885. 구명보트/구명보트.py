def solution(people, limit):
    answer = 0
    end = len(people) - 1
    people.sort(reverse = True)
    
    for i in range(len(people)) :
        if people[i] + people[end] <= limit :
            end -= 1
        answer += 1
        if end <= i :
            break
    return answer