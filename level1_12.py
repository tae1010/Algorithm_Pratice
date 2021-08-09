def solve(sum):
    for s in range(2, sum): 
        if sum % s == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    sum = 0
    count = 0
    
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if solve(sum) :
                    answer+=1
                    
    return answer
