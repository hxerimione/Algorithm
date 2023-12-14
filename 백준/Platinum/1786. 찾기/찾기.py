def getPi(p):
    m = len(p)
    j = 0
    pi=[0 for i in range(m)]
    for i in range(1,len(p)):
        while j>0 and p[i] != p[j] :
            j = pi[j-1]
        if p[i] == p[j] :
            j+=1
            pi[i] = j
    return pi

def KMP(T,P):
    answer=[]
    pi = getPi(P)
    n,m = len(T),len(P)
    j=0
    for i in range(n):
        while j>0 and T[i] != P[j] :
            j = pi[j-1]
        if T[i] == P[j] :
            if j == m-1:
                answer.append(i-m+2)
                j = pi[j]
            else:
                j+=1
    return answer

import sys
input = sys.stdin.readline
T = input().rstrip()
P = input().rstrip()
if len(T) < len(P):
    print(0)
    exit(0)
answer = KMP(T,P)
print(len(answer))
print(*answer)
