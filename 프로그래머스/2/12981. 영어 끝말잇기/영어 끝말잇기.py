def solution(n, words):
    answer = []
    stack=[]
    for i in range(len(words)):
        if words[i] in stack :
            return [i%n+1,i//n+1]
        
        if stack and stack[-1][-1] !=words[i][0]:
            return [i%n+1,i//n+1]
        elif len(words[i])<=1:
            print(i)
            return [i%n+1,i//n+1]
        stack.append(words[i])
        
        
    return [0,0]