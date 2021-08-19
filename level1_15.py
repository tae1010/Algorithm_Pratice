def solution(n):
    third = ""
    reverse = ""
    answer = 0
    j=0
    
    while n != 0:
        third += str(n%3)
        n = n//3
    print(third)
        
    for i in reversed(third):
        reverse += i
    print(reverse)
    
    for i in reverse:
        answer += (int(i) * 3**j)
        print(answer)
        j += 1
    return answer
