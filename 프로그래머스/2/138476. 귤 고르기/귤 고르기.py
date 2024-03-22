from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    q = []
    arr=defaultdict(int)
    for i in range(len(tangerine)):
        arr[tangerine[i]]+=1
    for key,v in arr.items():
        q.append((key,v))
    q = sorted(q,key = lambda x:x[1],reverse=True)
    tmp=0

    for a,b in q :
        tmp+=b
        answer+=1
        if tmp >= k:
            break
    return answer