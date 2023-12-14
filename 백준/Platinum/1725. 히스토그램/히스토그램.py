import sys
input = sys.stdin.readline
n= int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
answer=n*min(arr)
stack =[(0,arr[0])]
for i in range(1,len(arr)):
    while stack:
        if stack[-1][1] > arr[i]:
            a,b = stack.pop()
            if stack:
                width = i-stack[-1][0] -1
            else:
                width = i
            answer = max(answer,width*b)
        else:
            break
    stack.append((i,arr[i]))

while stack :
    a,b = stack.pop()
    if stack :
        width = n-1- stack[-1][0]
    else:
        width = n
    answer = max(answer,width *b)
    
print(answer)