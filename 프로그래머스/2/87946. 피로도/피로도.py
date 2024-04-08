from itertools import permutations 

def solution(k, dungeons):
    answer = 0
    for order in permutations(dungeons):
        v = k
        
        success = True
        cnt = 0
        for minval, useval in order:
            if v >= minval:
                v -= useval
                cnt += 1
            else:
                success = False
                break
        
        answer = max(answer, cnt)
            
    return answer