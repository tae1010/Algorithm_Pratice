def solution(array, commands):
    answer = []
    ans = [] #commands의 각 배열을 담을 변수
    
    for i in range(len(commands)):
        ans = array[commands[i][0]-1:commands[i][1]]
        ans.sort()
        k = ans[commands[i][2]-1]
        answer.append(k)

    return answer
