def solution(seoul):
    answer = ''
    count = 0
    solution = 0
    for i in seoul:
        if i == "Kim":
            break
        else:
            count += 1
    return "김서방은 "+ str(count) + "에 있다"
