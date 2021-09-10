def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    total = 0
    
    for i in range(a-1):
        total += days[i]
    total += b
        
    
    answer = day[total%7 - 1]
    return answer
