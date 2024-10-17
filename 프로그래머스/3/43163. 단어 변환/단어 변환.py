import math
def solution(begin, target, words):
    answer = []
    visited = [0 for _ in range(len(words))]
    def dfs(cur,count):
        if cur == target :
            answer.append(count)
        for i in range(len(words)):
            if visited[i] :
                continue
            tmp =0
            for w,c in zip(words[i],cur):
                if w!=c:
                    tmp+=1
            if tmp ==1 :
                # print(i,words[i])
                visited[i] =1
                dfs(words[i],count+1)
                visited[i] =0
            
    dfs(begin,0)
    if answer:
        return min(answer)
    else:
        return 0