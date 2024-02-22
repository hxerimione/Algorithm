
n = int(input())
dp = dict()
dp[0] = 0
dp[1] = 1
dp[2] = 1
def fibo(n):
    if dp.get(n) != None:
        return dp[n]
    # 짝수
    if n%2==0 :
        dp[n//2+1] = fibo(n//2+1)%1000000007
        dp[n//2-1] = fibo(n//2-1)%1000000007
        return dp[n//2+1]**2 - dp[n//2-1]**2
    # 홀수
    else:
        dp[n//2+1] = fibo(n//2+1)%1000000007
        dp[(n+1)//2-1] = fibo((n+1)//2-1)%1000000007
        return dp[n//2+1]**2 + dp[(n+1)//2-1]**2
    
print(fibo(n)%1000000007)