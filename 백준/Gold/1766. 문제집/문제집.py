import sys

import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
q=[]
degree= [0 for _ in range(n+1)]
graph= [[] for _ in range(n+1)]
answer=[]
for _ in range(m):
    f,b = map(int,input().split())
    degree[b] +=1
    graph[f].append(b)
for i in range(1,n+1):
    if degree[i] == 0 :
        q.append(i)

while q :
    tmp = heapq.heappop(q)
    answer.append(tmp)
    for g in graph[tmp] :
        degree[g]-=1
        if degree[g] ==0 :
            heapq.heappush(q,g)
print(*answer)