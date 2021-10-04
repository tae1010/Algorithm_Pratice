def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    s_lower = s.lower()
    for i in s_lower:
        if i =="p":
            p_count += 1
        elif i =="y":
            y_count += 1
    if p_count == y_count:
        return True
    elif p_count == 0 and y_count == 0:
        return True
    else:
        return False
