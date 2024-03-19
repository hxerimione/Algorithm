import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    degree = [0 for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    arr = list(map(int,input().split())) # 작년 순위
    for i in range(n):
        for j in range(i+1,n):
            graph[arr[i]].append(arr[j])
    m = int(input())
    if m ==0 :
        print(*arr)
        continue
    for _ in range(m):
        a,b = map(int,input().split())
        
        if b in graph[a] :
            graph[a].remove(b)
            graph[b].append(a)
        elif a in graph[b] :
            graph[b].remove(a)
            graph[a].append(b)
    q= deque()

    answer = []
    for i in range(1,n+1):
        degree[i] = n-1-len(graph[i])
        if degree[i] == 0 :
            q.append(i)
    while q :
        tmp = q.popleft()
        answer.append(tmp)
        for k in graph[tmp]:
            degree[k]-=1
            if degree[k] ==0 :
                q.append(k)
        
    if len(answer) <n :
        print("IMPOSSIBLE")
    else:
        print(*answer)
    

