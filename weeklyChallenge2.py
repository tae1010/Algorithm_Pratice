def score(sum):
    if sum>=90:
        return "A"
    elif sum>=80:
        return "B"
    elif sum>=70:
        return "C"
    elif sum>=50:
        return "D"
    else:
        return "F"

def solution(scores):
    answer = ""

    for i in range(len(scores)):
        my_score = scores[i][i] #내 점수를 저장할 변수
        other_score = [] #나를 포함한 나에게 점수를 준 사람들을 저장할 변수
        sum = 0
        
        for j in range(len(scores[i])):
            other_score.append(scores[j][i])
            
        if max(other_score) == my_score or min(other_score) == my_score:
            if other_score.count(my_score) <= 1:
                del other_score[i]
        
        for i in other_score:
            sum += i
            
        sum = sum/len(other_score)
        answer += score(sum)

    return answer
