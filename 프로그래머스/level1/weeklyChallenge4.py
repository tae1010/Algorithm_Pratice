def solution(table, languages, preference):
    answer = 'ZZZZZZZZ'
    score_dic = {lang: score for lang, score in zip(languages, preference)}
    max_score = 0
    for row in table:
        r = row.split(' ')
        curr_score = 0
        for i in range(1, len(r)):
            curr_score += score_dic.get(r[i], 0) * (6-i)
        if max_score < curr_score:
            max_score = curr_score
            answer = r[0]
        elif max_score == curr_score and answer > r[0]:
            answer = r[0]


    return answer
