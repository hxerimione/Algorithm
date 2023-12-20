import sys
input = sys.stdin.readline
N,L = map(int,input().split())
A = list(map(int,input().split()))
from collections import deque
q = deque([])
answer=[]
for i in range(N):
    if q and q[0][0] <i-L+1:
        q.popleft()
    while len(q)>=1 and q[-1][1] >=A[i] :
        q.pop()
    q.append((i,A[i]))
    answer.append(q[0][1])
print(*answer)

