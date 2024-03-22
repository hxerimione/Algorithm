def solution(s):

    n=len(s)
    cnt =0
    zero=0
    while s != '1':
        cnt+=1
        #1번
        one = s.count('1')
        zero += n-one
        
        # s = '1'*one
        #2번
        s = bin(one)[2:]
        n= len(s)


    return [cnt,zero]