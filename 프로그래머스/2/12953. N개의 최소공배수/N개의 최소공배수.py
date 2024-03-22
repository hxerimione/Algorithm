def solution(arr):
    answer = arr[0]
    from math import gcd
    for i in range(len(arr)-1):
        tmp  = gcd(answer,arr[i+1])
        answer = tmp *(answer//tmp)*(arr[i+1]//tmp)
        
    return answer