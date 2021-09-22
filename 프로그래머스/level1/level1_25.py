def solution(s):
    answer = ''
    s_len = len(s)
    
    if s_len%2 == 1:
        return s[int(s_len//2)]
    else:
        answer += s[int(s_len//2)-1]
        answer += s[int(s_len//2)]
        return answer
