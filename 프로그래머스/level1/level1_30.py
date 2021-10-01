def solution(s): 
    word = s.split(" ")
    
    for k in range(len(word)): 
        word_list = list(word[k]) 
        for i in range(len(word_list)): 
            if i % 2 == 0: 
                word_list[i] = word_list[i].upper() 
            elif i % 2 == 1: 
                word_list[i] = word_list[i].lower() 
        word[k] = "".join(word_list) 
    answer = " ".join(word)
    return answer
