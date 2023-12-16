import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

stack=[]
stack.append(arr[0])

#idx=0
for i in range(n):
    if stack[-1] < arr[i] :
        stack.append(arr[i])
    else:
        l,r = 0,len(stack)
        while l<r:
            mid = (l+r)//2
            if arr[i] <= stack[mid]:
                r =mid
            else:
                l = mid+1
        stack[r]= arr[i]
#print(stack)
#print(pi)
print(len(stack))