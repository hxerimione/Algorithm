import sys
input = sys.stdin.readline

N,K = map(int,input().split())
if N==K:
    print(0)
    exit()
visited = [[-1]*2 for _ in range(500001)]

q = [N]
time = 1
K +=1
while True : 
    if K > 500000 :
        break
    nextQ=[]
    for point in q :
        for next in [point-1,point+1,2*point]:
            if 0<=next<=500000 and visited[next][time%2] == -1:
                nextQ.append(next)
                visited[next][time%2] = time

    if visited[K][time%2]!= -1 :
        print(time)
        exit()
    time +=1
    K += time
    q = nextQ
print(-1)

