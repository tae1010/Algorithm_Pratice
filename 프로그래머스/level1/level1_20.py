def solution(numbers):
    sum = 45
    for i in numbers:
        sum -= i
    return sum
