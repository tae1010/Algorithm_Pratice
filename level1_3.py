def solution(answers):
    supoza = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    count = [0,0,0]
    
    for i in range(len(answers)):
        for j in range(3):
            if len(answers) > len(supoza[j]):
                supoza[j] = supoza[j] * (len(answers)//len(supoza[j]) + 1)
            
            if answers[i] == supoza[j][i]:
                count[j] += 1
    
    answer = []

    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)

    return answer
