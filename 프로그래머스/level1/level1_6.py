def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num2 = ["0","1","2","3","4","5","6","7","8","9"]
    answer = []
    
    for i in range(10):
        s = s.replace(num[i],num2[i])

    
    return int(s)
