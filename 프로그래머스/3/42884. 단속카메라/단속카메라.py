def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x : (x[1],x[0]) )
    stack = []
    print(routes)
    for a,b in routes :
        if not stack :
            answer+=1
            stack.append((a,b))
            continue
        if stack[-1][1]<a:
            #안겹치면
            answer+=1
            stack.append((a,b))
        else:
            #겹치면
            continue
            
            
    return answer