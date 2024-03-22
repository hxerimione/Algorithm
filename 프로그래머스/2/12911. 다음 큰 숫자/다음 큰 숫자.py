def solution(n):
    answer = 0
    one = str(bin(n)[2:]).count('1')
    while True:
        n+=1
        if str(bin(n)[2:]).count('1') == one :
            answer = n
            break
    return answer