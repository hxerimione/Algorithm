import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = []
import math
node_n = (2**int((math.log2(n)+2)))
tree = [0]*(node_n+1)
for _ in range(n):
    arr.append(int(input()))

def make_seg(idx, start, end):
    mid = (start+end)//2
    if start == end : 
        tree[idx] = arr[start] 
        return tree[idx]
    l = make_seg(idx*2 , start,mid)
    r = make_seg(idx*2+1 , mid+1, end)
    tree[idx] = l+r
    return tree[idx]
    
def update(target,idx,start,end):
    if start> target or target >end:
        return tree[idx]
    if start == end : 
        tree[idx] = arr[start] 
        return tree[idx]
    mid =(start+end)//2
    l = update(target,idx*2,start,mid)
    r = update(target,idx*2+1,mid+1,end)
    tree[idx] = l+r
    return l + r
def find(idx,start,end):
    if start>c or end<b :
        return 0 
    if start >=b and end <=c :
        return tree[idx]
    mid =(start+end)//2
    l = find(idx*2,start,mid)
    r = find(idx*2+1,mid+1,end)
    return l + r

make_seg(1,0,n-1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        arr[b-1] = c
        update(b-1,1,0,n-1)
    elif a==2:
        # print("tree",tree)
        b,c = b-1,c-1
        print(find(1,0,n-1))
