import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer=0
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    S = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        S[i] = S[i-1] + arr[i]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1-i):
            dp[j][j+i] = min([dp[j][j+k] + dp[j+k+1][j+i] for k in range(i)]) + S[j+i]-S[j-1]
            
    print(dp[1][n])




