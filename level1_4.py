def solution(lottos, win_nums):
    answer = []
    min = 0
    max = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                min+=1
        if i == 0:
            max+=1

    answer = [7-(max+min), 7-min]
    
    for i in range(len(answer)):
        if answer[i] == 7 : 
            answer[i] = 6

    return answer
