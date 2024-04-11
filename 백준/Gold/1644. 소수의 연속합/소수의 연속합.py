import sys
input = sys.stdin.readline
import math
n = int(input())
if n ==1:
    print(0)
    exit(0)
if n==2:
    print(1)
    exit(0)
prime = [False,False]+ [True]*(n-1)
arr=[]
for i in range(2,n+1):
    #소수인지 확인
    if prime[i]:
        arr.append(i)
        for j in range(2*i,n+1,i):
            prime[j] = False
        
l,r = 0,0
answer=0
while r<=len(arr):
    s= sum(arr[l:r])
    if s>n:
        l+=1
    elif s<n:
        r+=1
    else:
        answer+=1
        l+=1
        r+=1
print(answer)