def solution(n):
    answer = 1
    l,r=1,1
    num = [i for i in range(n+1)]
    s = 1
    while l!= n :
        if s < n :
            r+=1
            s+=r
        elif s>n:
            s-=l
            l+=1
        else:
            print(l,r)
            answer+=1
            s-=l
            l+=1
            r+=1
            s+=r
    print(answer)
    return answer