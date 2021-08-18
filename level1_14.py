def first(new_id):
    return new_id.lower()

def second(new_id):
    answer = ""
    for i in new_id:
        if i.islower()  or i.isdigit() or i in ['-', '_', '.']:
            answer += i
    return answer

def third(new_id):
    while ".." in new_id:
        new_id = new_id.replace("..",".")
    return new_id

def fourth(new_id):
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
        
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id

def fifth(new_id):
    answer = "a"
    if len(new_id) == 0:
        return answer
    return new_id

def sixth(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    return new_id

def seventh(new_id):
    while len(new_id) <= 2 :
        new_id += new_id[-1]
    return new_id
        
def solution(new_id):
    answer = ''
    answer = seventh(sixth(fifth(fourth(third(second(first(new_id)))))))

    print(answer)
    return answer
