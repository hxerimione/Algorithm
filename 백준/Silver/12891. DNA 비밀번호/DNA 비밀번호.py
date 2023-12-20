import sys
input = sys.stdin.readline
N,M = map(int,input().split())
s = input().rstrip()
A,C,G,T = map(int,input().split())
dic = {'A':0, 'C':0, 'G':0, 'T':0}
answer=0
for i in range(N):
    if i <M-1:
        dic[s[i]] +=1
    elif i==M-1 :  
        dic[s[i]]+=1
        if dic['A']>=A and dic['C']>=C and dic['G']>=G and dic['T']>=T:
            answer+=1
    else:
        dic[s[i-M]]-=1
        dic[s[i]]+=1
        if dic['A']>=A and dic['C']>=C and dic['G']>=G and dic['T']>=T:
            answer+=1

print(answer)

