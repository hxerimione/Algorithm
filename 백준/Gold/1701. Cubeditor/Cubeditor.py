
import sys
input = sys.stdin.readline

def getMaxPi(p):
    pi = [0]*len(p)
    j=0
    for i in range(1,len(p)):
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j+=1
            pi[i] = j
    return max(pi)

answer=0
s = input().rstrip()
for i in range(len(s)):
    answer = max(getMaxPi(s[i:]),answer)
print(answer)