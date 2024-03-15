import sys

input = sys.stdin.readline

#minheap,maxheap
from heapq import heappush,heappop 
minheap = []
maxheap = []
n= int(input())

a = int(input())
print(a)
b = int(input())
if a<=b :
    print(a)
    heappush(minheap,-a)
    heappush(maxheap,b)
else:
    print(b)
    heappush(minheap,-b)
    heappush(maxheap,a)
for _ in range(n-2):
    a = int(input())
    minq = heappop(minheap)
    maxq = heappop(maxheap)
    if -minq >= a:
        heappush(minheap,-a)
        if len(minheap)>len(maxheap)+1:
            heappush(maxheap,-minq)
            heappush(maxheap,maxq)
        else:
            heappush(minheap,minq)
            heappush(maxheap,maxq)
    elif maxq <= a :
        heappush(maxheap,a)
        if len(maxheap)>len(minheap):
            heappush(minheap,minq)
            heappush(minheap,-maxq)
        else:
            heappush(minheap,minq)
            heappush(maxheap,maxq)
        
    else:
        heappush(minheap,minq)
        heappush(maxheap,maxq)
        if len(minheap)==len(maxheap):
            heappush(minheap,-a)
        else:
            heappush(maxheap,a)
    # print(minheap,maxheap)
    print(-minheap[0])
