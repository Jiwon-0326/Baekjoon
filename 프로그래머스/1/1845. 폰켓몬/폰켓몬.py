def solution(nums):
    nums_ = set(nums)
    if len(nums_) >= len(nums)/2 :
        return len(nums)/2
    else :
        return len(nums_)