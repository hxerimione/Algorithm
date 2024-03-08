import sys
input = sys.stdin.readline
n= int(input())
nums = [0] * 1000001
tree = [0] * (2**21)

def update(target, diff , idx, start, end):
    if end < target or target < start:
        return 

    tree[idx] += diff
    if start != end:
        update(target, diff , idx*2 , start , (start+end)//2)
        update(target, diff , idx*2+1, (start+end)//2 + 1 , end)

def pick(count , idx, start, end):
        
    if start == end: # 리프노드 도달
        return start
    
    else:
        if tree[idx*2] >= count:
            return pick(count , idx*2, start, (start+end)//2)
        else:
            return pick(count - tree[idx*2] , idx*2 + 1 , (start+end)//2 + 1, end)


for _ in range(n):
    arr = list(map(int,input().split()))
    if arr[0] > 1:
        update(arr[1], arr[2], 1, 1, 1000001)
        nums[arr[1]] += arr[1]
        
    else:
        eat = pick(arr[1] , 1, 1, 1000001)
        print(eat)
        update(eat, -1, 1, 1, 1000001)
        nums[eat] += -1

