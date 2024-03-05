import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
#2차원 리스트에 트리 저장
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

def BFS(start):
    q=deque()
    q.append((start,0))
    visited = [-1]*(V+1)
    visited[start] = 0
    res = [0,0]
    while q:
        cnt_node, cnt_dist = q.popleft()
        for adj_node, adj_dist in tree[cnt_node]:
            if visited[adj_node] == -1 : #방문 안했으면
                cal_dist = adj_dist + cnt_dist
                q.append((adj_node,cal_dist))
                visited[adj_node] = cal_dist
                if res[1] < cal_dist :
                    res = [adj_node,cal_dist]
    return res

point,_ = BFS(1)
print(BFS(point)[1])

