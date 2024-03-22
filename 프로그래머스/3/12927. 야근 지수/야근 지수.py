import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n :
        return 0
    works.sort(reverse = True)
    m = len(works)
    q=[]
    for i in range(m):
        heapq.heappush(q,-works[i])
    for _ in range(n):
        a = heapq.heappop(q)
        a+=1
        heapq.heappush(q,a)
    
    for i in range(m):
        answer+=q[i]**2
    return answer