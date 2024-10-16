def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))];
    
    while priorities : 
        a = priorities.pop(0)
        p = idx.pop(0)
        
        if priorities and max(priorities) > a :
            priorities.append(a)
            idx.append(p)
        else:
            answer+=1
            if p == location : 
                return answer
    return answer