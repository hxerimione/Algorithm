def solution(string):
    answer = ''
    flag = False
    answer += string[0].upper()
    for i in range(1,len(string)) :
        if flag : 
            flag = False
            answer += string[i].upper()
        else:
            answer += string[i].lower()
        if string[i] == ' ':
            flag = True
        
    return answer