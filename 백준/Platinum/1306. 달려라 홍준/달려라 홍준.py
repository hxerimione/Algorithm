import sys
input = sys.stdin.readline
from collections import deque
N,k = map(int,input().split())
number =list(map(int,input().split()))
q = deque([])
q.append((0,number[0]))
answer=[]
for i in range(2*(k-1)):
    while len(q)>=1 and q[-1][1] <= number[i] :
        q.pop()
    
    q.append((i,number[i]))

for i in range(2*(k-1),N):
    if q and q[0][0]<i-(k-1)*2 :
        q.popleft()
    while len(q)>=1 and q[-1][1] <= number[i]:
        q.pop()
    q.append((i,number[i]))
    answer.append(q[0][1])
print(*answer)