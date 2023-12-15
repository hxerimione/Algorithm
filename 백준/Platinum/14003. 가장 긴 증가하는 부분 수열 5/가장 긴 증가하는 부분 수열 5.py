
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
lis = [0]*n
lis[0] = arr[0]
record = [0]*n
tmp=0
j=0
for i in range(1,n):
    if lis[j] < arr[i] :
        lis[j+1] = arr[i]
        j+=1
        record[i] = j
    else:
        #print("i",i,j)
        l,r = 0,j
        while l<r:
            mid = (l+r)//2
            #print("mid",mid,lis[l],arr[i])
            if lis[mid]< arr[i]:
                #print("l",l,r)
                l = mid+1
                tmp = l
            else:
                #print("r",l,r)
                r = mid
                tmp = r
        lis[tmp] = arr[i]
        record[i] =tmp
        
idx = max(record)
answer=[]
for i in range(n-1,-1,-1):
    if record[i] == idx :
        answer.append(arr[i])
        idx-=1
#print(lis)
#print(record)
answer.sort()
print(len(answer))
print(*answer)