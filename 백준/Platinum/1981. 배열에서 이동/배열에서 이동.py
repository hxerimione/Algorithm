import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
#전체 최소,최대 값
leftMin = 200
rightMax = 0
for _ in range(N):
    tmp = list(map(int,input().split()))
    leftMin = min(leftMin,min(tmp))
    rightMax = max(rightMax,max(tmp))
    graph.append(tmp)
arr = [[(0,200)]* N for _ in range(N)]

dx,dy= [-1,0,1,0],[0,-1,0,1]


leftMax = min(graph[0][0],graph[N-1][N-1])
rightMin = max(graph[0][0],graph[N-1][N-1])
ans = 200
left,right = leftMin,rightMin

def bfs() :
    q = deque()
    q.append((0,0))
    visited = [[-1]*N for _ in range(N)]
    while q:
        a,b = q.popleft()
        if a==N-1 and b==N-1 :
            return True
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if left <= graph[nx][ny] <= right and visited[nx][ny]==-1 :
                    visited[nx][ny] = 0
                    q.append((nx,ny))
    return False

while leftMin <=left<=leftMax and rightMin <=right<=rightMax :
    leftFlag,rightFlag = 0,0
    # 끝까지 이동
    # print(left,right)
    if bfs():
        ans = min(ans,right-left)
        left +=1
        leftFlag = 1
    else:
        #이미 한번이상 성공, 다른 범위 확인
        if leftFlag and rightFlag : 
            left+=1
            right+=1
        else:
            right+=1
            rightFlag = 1

print(ans)



