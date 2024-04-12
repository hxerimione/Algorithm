import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visit = [False for _ in range(n+1)]
    answer=n
    for i in range(1,n+1):
        if visit[i]:
            continue
        else:
            tmp = i
            st=[]
        
        while True :

            visit[tmp] = True
            target = arr[tmp]
            st.append(tmp)
            if visit[target]:
                if target in st :

                    answer -= len(st) - st.index(target)
                break
            tmp = target

    print(answer)