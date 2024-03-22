def solution(people, limit):
    answer = 0
    people.sort()
    l,r = 0,len(people)-1
    from collections import deque
    q = deque(people)
    while q :
        if l<r:
            if q[l] + q[r] <=limit :
                answer+=1
                l+=1
                r -=1
                q.pop()
            else:
                answer+=1
                q.pop()
                r-=1
        elif l==r:
            answer+=1
            l+=1
            q.pop()
        else:
            break
            
        
            
                
    return answer