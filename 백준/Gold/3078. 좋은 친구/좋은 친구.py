import sys
input = sys.stdin.readline
N,K = map(int,input().split())
name =[]
for i in range(N):
    na = input().rstrip()
    name.append(len(na))
cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

answer=0

for i in range(N):
    if i>0:
        if i-K<=0:
            answer += cnt[name[i]]
        else:
            cnt[name[i-K-1]]-=1
            answer += cnt[name[i]]
    cnt[name[i]] +=1
print(answer)
