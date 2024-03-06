import sys
import math
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
tree = [0]*(2**int(math.log2(N)+2)+2)

swap=0
def sort(start,end):
    global swap
    if start<end:
        mid = (start+end)//2
        sort(start,mid)
        sort(mid+1,end)
        tmp=[]
        x,y = start,mid+1
        while x<=mid and y<=end:
            if arr[x] <= arr[y] :
                tmp.append(arr[x])
                x+=1
            else:
                tmp.append(arr[y])
                y+=1
                swap += (mid-x)+1
        if x<=mid:
            tmp += arr[x:mid+1]
        if y<=end:
            tmp += arr[y:end+1]
        #갱신
        for i in range(len(tmp)):
            arr[start+i] = tmp[i]
sort(0,N-1)
print(swap)