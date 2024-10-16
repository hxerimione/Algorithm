def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, tmp):
        if idx ==n :
            if tmp == target:
                return 1
            else:
                return 0
        return dfs(idx+1,tmp+numbers[idx]) + dfs(idx+1,tmp-numbers[idx])
    return dfs(0,0)