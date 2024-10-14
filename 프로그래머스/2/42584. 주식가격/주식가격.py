def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    stack=[]
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            tmp = stack.pop()
            answer[tmp] = i-tmp
        stack.append(i);
    return answer