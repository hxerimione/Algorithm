
import sys
input = sys.stdin.readline


def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

while True :
    
    s = input().rstrip()
    if s == ".":
        exit(0)
    n = len(s)  
    arr = getMyDivisor(n)
    answer = []
    for a in arr :
        ss = s[:a]*(n//a)
        if ss == s :
            answer.append(n//a)
    print(max(answer))
