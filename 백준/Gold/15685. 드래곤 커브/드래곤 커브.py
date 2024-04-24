import sys
input = sys.stdin.readline
T = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]
arr = [[0]*101 for _ in range(101)]
answer=0
for _ in range(T):
    
    x,y,d,g = map(int,input().split())
    arr[x][y] = 1
    route = str(d)
    for _ in range(g):
        for i in range(len(route)-1,-1,-1):
            route += str((int(route[i])+1)%4)
    for r in route:
        x += dx[int(r)]
        y += dy[int(r)]
        arr[x][y] = 1
            
        
for i in range(100):
    for j in range(100):
        if arr[i][j] :
            if arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:

                answer+=1
print(answer)