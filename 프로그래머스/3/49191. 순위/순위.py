def solution(n, results):
    answer = 0
    arr = [[0 for _ in range(n+1)]for _ in range(n+1)]
    degree = [0 for _ in range(n+1)]
    back=[0 for _ in range(n+1)]
    for a,b in results :
        arr[a][b] = 1
        degree[b] +=1
        back[a]+=1
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if arr[i][k] ==1 and arr[k][j] ==1 and arr[i][j]==0:

                    arr[i][j]=1
                    degree[j]+=1
                    back[i]+=1
    
    for i in range(n+1):
        if degree[i]+back[i] == n-1 :
            answer+=1
        
        
    return answer