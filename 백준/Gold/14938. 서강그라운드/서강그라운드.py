import sys
import heapq
input = sys.stdin.readline
n,m,r = map(int,input().split())
cost = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))
q=[]
answer=0
for i in range(1,n+1): #시작노드
    able = [False for _ in range(n+1)]
    node_cost =0
    for j in range(1,n+1): #도착노드
        heapq.heappush(q,(i,0))
        while q :
            t,d = heapq.heappop(q)
            for node,distance in graph[t]:
                if d + distance <=m :
                    if not able[node]:
                        heapq.heappush(q,(node,d+distance))
                else:
                    continue
            able[t] = True
    for k in range(1,n+1):
        if able[k]:
            node_cost += cost[k]
    answer = max(answer,node_cost)
print(answer)