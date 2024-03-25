def solution(progresses, speeds):
    answer = []
    stack=[]
    for p,s in zip(progresses,speeds):
        if (100-p)%s == 0 :
            tmp =(100-p)//s
        else:
            tmp = (100-p)//s +1
        if stack :
            if stack[-1][0]>=tmp :
                stack[-1][1] +=1
            else:
                stack.append([tmp,1])
        else:
            stack.append([tmp,1])
    for a,b in stack:
        answer.append(b)
    return answer