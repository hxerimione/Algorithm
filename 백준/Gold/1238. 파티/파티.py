import sys
import heapq 
input = sys.stdin.readline
N,M,X = map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))

def dijkstra(start):
    q=[]
    distance = [1e9] * (N+1)
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q :
        dist, now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i,c in graph[now]:
            cost = c+ dist
            if distance[i] > cost :
                distance[i] = cost
                heapq.heappush(q,(cost,i)) 
    return distance

answer=[]
for i in range(1,N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    answer.append(go[X] + back[i])
print(max(answer))

