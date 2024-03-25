from collections import defaultdict
def solution(clothes):
    answer = 1
    
    dict = defaultdict(int)
    for cloth in clothes :
        dict[cloth[1]] +=1
        
    for d in dict.values():
        answer *= d+1
    answer-=1
    return answer