def solution(numbers, hand):
    answer = ''
    left_last = 10
    right_last = 12
    
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            left_last = n
        elif n in [3,6,9]:
            answer+='R'
            right_last = n
        else:
            n = 11 if n == 0 else n
            
            absL = abs(n-left_last)
            absR = abs(n-right_last)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer+='R'
                right_last = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                left_last = n
            else:
                if hand == 'left':
                    answer+='L'
                    left_last = n
                else:
                    answer+='R'
                    right_last = n
                
    return answer
