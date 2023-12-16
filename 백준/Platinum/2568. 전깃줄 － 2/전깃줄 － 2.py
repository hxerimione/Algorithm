import sys
input = sys.stdin.readline
n = int(input())
arr=[]
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
stack=[(0,0)]*n
stack[0]= arr[0]

pi = [0]*n

#idx=0
j=0
mid=0
for i in range(1,n):
    if stack[j][1] < arr[i][1] :
        j+=1
        stack[j] = arr[i]
        pi[i] = j
    else:
        l,r = 0,j
        while l<r:
            mid = (l+r)//2
            if arr[i][1] <= stack[mid][1]:
                r =mid
            
            else:
                l = mid+1
        
        stack[r]= arr[i]
        pi[i] = r
m = max(pi)
from collections import deque
answer=deque()
for i in range(n-1,-1,-1):
    if pi[i] == m :
        m-=1
    else:
        answer.appendleft(arr[i])
# print(arr)
# print(stack)
# print(pi)
# print(answer)
print(len(answer))

for a,b in answer:
    print(a)
