def solution(s):
    answer = 0
    def val(s):
        stack=[]
        for i in range(len(s)):
            if stack:
                if stack[-1] == '[' and s[i] ==']':

                    stack.pop()
                elif stack[-1] == '{' and s[i] =='}':

                    stack.pop()
                elif stack[-1] == '(' and s[i] ==')':

                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True
    for x in range(len(s)):
        #올바른지
        s = s[1:]+s[0]

        if val(s):
            #올바르면
            answer+=1
    return answer