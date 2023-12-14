import sys
while True :
    arr =list(map(int,input().split()))
    if arr[0] ==0:
        break
    n = arr[0]
    m = max(arr)
    #answer = n*min(arr[1:])
    answer=n*min(arr[1:])
    stack =[(1,arr[1])]
    for i in range(1,len(arr)):
        while len(stack)>0:
            if stack[-1][1] > arr[i]:
                a,b = stack.pop()
                if stack:
                    width = i-stack[-1][0] -1
                else:
                    width = i-1
                answer = max(answer,width*b)
            else:
                break
        stack.append((i,arr[i]))
    while stack :
        a,b = stack.pop()
        if stack :
            width = n- stack[-1][0]
        else:
            width = n
        answer = max(answer,width *b)
    
    print(answer)