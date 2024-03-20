def solution(s):
    answer = True
    stack=[]
    for i  in range(len(s)):
        if len(stack)>0 and stack[-1] == '(' and s[i] == ')':
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack)== 0 :
        return True
    else:
        return False
    