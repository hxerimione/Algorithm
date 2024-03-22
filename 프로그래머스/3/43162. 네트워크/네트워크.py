
from collections import deque
def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]
    q=deque()
    
    for i in range(n):
        for j in range(i,n):
            if visit[j] ==1 :
                continue
            if computers[i][j] == 1:
                visit[i] =1
                q.append(j)
        if q:
            answer+=1
        while q :
            a = q.popleft()
            visit[a] =1
            for k in range(n):
                if computers[a][k] == 1 and visit[k] ==0:
                    q.append(k)

    return answer