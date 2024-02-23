import sys,math
input = sys.stdin.readline
n,m = map(int,input().split())
sys.setrecursionlimit(10 ** 8)
arr=[]
for _ in range(n):
    arr.append(int(input()))
arrlen = len(arr)
node= int(math.log2(arrlen))+2

seg = [0]*(2**node)
# print("s",len(seg))
def makeSeg(idx,s,e):
    if s==e:
        seg[idx] = arr[s]
        return seg[idx]
    mid = (s+e)//2
    l = makeSeg(idx*2, s,mid)
    r = makeSeg(idx*2+1,mid+1,e)
    seg[idx] = min(l,r)
    return seg[idx]
def find(idx,s,e):
    if e<a or s>b:
        return 1000000001
    if s>=a and e<=b:
        return seg[idx]
    mid = (s+e)//2
    l = find(idx*2, s,mid)
    r = find(idx*2+1,mid+1,e)
    return min(l,r)

makeSeg(1,0,arrlen-1)
for _ in range(m):
    #실제 실행되는 부분
    a,b = map(int,input().split())
    a,b = a-1,b-1
    print(find(1,0,arrlen-1))
