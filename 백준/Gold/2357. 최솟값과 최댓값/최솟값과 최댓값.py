import sys,math
input = sys.stdin.readline
n,m = map(int,input().split())
sys.setrecursionlimit(10 ** 8)
arr=[]
def make_seg(idx,s,e):
    mid = (s+e)//2
    if s==e :
        seg[idx] = (arr[s],arr[s])
        return seg[idx]
    l = make_seg(idx*2,s,mid)
    r = make_seg(idx*2+1,mid+1,e)
    seg[idx] = (min(l[0],r[0]),max(l[1],r[1]))
    return seg[idx]
def find(s,e,idx):
    if s>b or e<a:
        return (1000000000,0)
    mid = (s + e) // 2
    if a <= s and e <= b:  
        return seg[idx]
    else:
        l = find(s, mid, idx * 2)
        r = find(mid + 1, e, idx * 2 + 1)
        return (min(l[0], r[0]), max(l[1], r[1]))
for _ in range(n):
    arr.append(int(input()))

node_n = 1 << (math.ceil(math.log2(n)) + 1)
seg = [0]*node_n
make_seg(1,0,len(arr)-1)
for _ in range(m):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    ans = find(0,len(arr)-1,1)
    print(*ans)