import sys
from collections import deque 
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    q = deque()
    degree = [0 for _ in range(n+1)]
    graph= [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for _ in range(k):
        f,b = map(int,input().split())
        degree[b] +=1
        graph[f].append(b)
    
    for i in range(1,n+1):#진입차수 0인거 찾아서 큐에 넣기
        if degree[i]==0:
            q.append(i)
            dp[i]=time[i]
 
    # print(graph)
    # print(degree)
    while q:
        a=q.popleft()
        for i in graph[a]:
            degree[i]-=1#진입차수 줄이고
            dp[i]=max(dp[a]+time[i],dp[i])#dp를 이용해 건설비용 갱신
            if degree[i]==0:
                q.append(i)
 
 
    ans=int(sys.stdin.readline())
    print(dp[ans])


    