def solution(board, moves):
    result = []
    answer = 0
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                result.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                if len(result) >= 2:
                    if result[-1] == result[-2]:
                        answer += 2
                        result.pop(-1)
                        result.pop(-1)
                break
    print(result)
    return answer
