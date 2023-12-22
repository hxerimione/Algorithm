import sys
input = sys.stdin.readline
from collections import defaultdict
N,d,k,c = map(int,input().split())
number =[]
for i in range(N):
    number.append(int(input()))
d = defaultdict(int)
d[c] = 1
cnt =1
for i in range(k):
    if d[number[i]] == 0:
        cnt +=1
    d[number[i]]+=1
answer = cnt
for i in range(k,N+k-1):
    d[number[i-k]] -= 1
    if d[number[i-k]] == 0 :
        cnt -=1
    d[number[i%N]]+=1
    if d[number[i%N]] == 1:
        cnt+=1
    answer = max(answer,cnt)
print(answer)